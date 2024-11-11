from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import requests
import os
from urllib.parse import urlencode
import discord
from discord.ext import commands

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL connection details
db_host = 'localhost'
db_user = 'your_mysql_username'
db_password = 'your_mysql_password'
db_name = 'integrated_app'

# Netflix API settings
netflix_api_key = 'your_netflix_api_key'
netflix_api_base_url = 'https://api.netflix.com/v1'

# Spotify API settings
spotify_client_id = 'your_spotify_client_id'
spotify_client_secret = 'your_spotify_client_secret'
spotify_redirect_uri = 'http://localhost:5000/spotify/callback'
spotify_scope = 'user-library-read playlist-modify-public'

# Discord bot settings
discord_bot_token = 'your_discord_bot_token'
discord_guild_id = 'your_discord_guild_id'

# Connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

# Initialize Discord bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Netflix search
@app.route('/netflix/search', methods=['GET', 'POST'])
def netflix_search():
    if request.method == 'POST':
        query = request.form['query']
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Search Netflix API for movies and series
        url = f"{netflix_api_base_url}/search?q={query}&api_key={netflix_api_key}"
        response = requests.get(url)
        results = response.json()['results']
        
        # Save search results to MySQL database
        for result in results:
            title = result['title']
            type = result['type']
            cursor.execute("INSERT INTO netflix_titles (title, type) VALUES (%s, %s)", (title, type))
        conn.commit()
        cursor.close()
        conn.close()
        
        return render_template('netflix_search.html', results=results)
    
    return render_template('netflix_search.html')

# Spotify search and playlist creation
@app.route('/spotify/login')
def spotify_login():
    params = {
        'client_id': spotify_client_id,
        'response_type': 'code',
        'redirect_uri': spotify_redirect_uri,
        'scope': spotify_scope
    }
    return redirect('https://accounts.spotify.com/authorize?' + urlencode(params))

@app.route('/spotify/callback')
def spotify_callback():
    code = request.args.get('code')
    
    # Exchange the authorization code for an access token
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': spotify_redirect_uri,
        'client_id': spotify_client_id,
        'client_secret': spotify_client_secret
    }
    response = requests.post('https://accounts.spotify.com/api/token', data=data)
    access_token = response.json()['access_token']
    
    # Save the access token to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO spotify_users (access_token) VALUES (%s)", (access_token,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('spotify_search'))

@app.route('/spotify/search', methods=['GET', 'POST'])
def spotify_search():
    if request.method == 'POST':
        query = request.form['query']
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Search Spotify API for songs
        access_token = get_spotify_access_token(cursor)
        headers = {'Authorization': f'Bearer {access_token}'}
        url = f'https://api.spotify.com/v1/search?q={query}&type=track'
        response = requests.get(url, headers=headers)
        results = response.json()['tracks']['items']
        
        # Save search results to MySQL database
        for result in results:
            title = result['name']
            artist = result['artists'][0]['name']
            cursor.execute("INSERT INTO spotify_tracks (title, artist) VALUES (%s, %s)", (title, artist))
        conn.commit()
        cursor.close()
        conn.close()
        
        return render_template('spotify_search.html', results=results)
    
    return render_template('spotify_search.html')

# Discord video/song streaming
@app.route('/discord/stream', methods=['GET', 'POST'])
def discord_stream():
    if request.method == 'POST':
        url = request.form['url']
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Save the video/song URL to the database
        cursor.execute("INSERT INTO discord_stream_urls (url) VALUES (%s)", (url,))
        conn.commit()
        cursor.close()
        conn.close()
        
        # Send a message to the Discord server
        guild = bot.get_guild(discord_guild_id)
        channel = guild.text_channels[0]
        channel.send(f"New video/song added to the playlist: {url}")
        
        return redirect(url_for('discord_stream'))
    
    # Retrieve the saved video/song URLs from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM discord_stream_urls")
    urls = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    
    return render_template('discord_stream.html', urls=urls)

# Discord bot events
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def play(ctx, url: str):
    # Add the video/song URL to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO discord_stream_urls (url) VALUES (%s)", (url,))
    conn.commit()
    cursor.close()
    conn.close()
    
    await ctx.send(f"Added {url} to the playlist!")

# Helper functions
def get_spotify_access_token(cursor):
    cursor.execute("SELECT access_token FROM spotify_users ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

if __name__ == '__main__':
    # Create the MySQL database and tables if they don't exist
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS integrated_app")
    cursor.execute("CREATE TABLE IF NOT EXISTS netflix_titles (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), type VARCHAR(50))")
    cursor.execute("CREATE TABLE IF NOT EXISTS spotify_users (id INT AUTO_INCREMENT PRIMARY KEY, access_token TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS spotify_tracks (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), artist VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS discord_stream_urls (id INT AUTO_INCREMENT PRIMARY KEY, url TEXT)")
    cursor.close()
    conn.close()
    
    # Run the Flask app and start the Discord bot
    bot.run(discord_bot_token)
    app.run(debug=True)
