# app.py

from flask import Flask, render_template, request, jsonify
from netflix_api import get_season_episodes
from spotify_api import get_spotify_data
from discord_api import send_discord_message
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/netflix/episodes', methods=['GET'])
def netflix_episodes():
    season_id = request.args.get('season_id')
    episodes = get_season_episodes(season_id)
    return jsonify(episodes)

@app.route('/spotify/data', methods=['GET'])
def spotify_data():
    endpoint = request.args.get('endpoint')
    params = request.args.to_dict(flat=True)
    params.pop('endpoint', None)
    data = get_spotify_data(endpoint, params)
    return jsonify(data)

@app.route('/discord/message', methods=['POST'])
def discord_message():
    data = request.json
    channel_id = data.get('channel_id')
    message = data.get('message')
    success = send_discord_message(channel_id, message)
    return jsonify({"success": success})

@app.route('/db/query', methods=['GET'])
def db_query():
    query = request.args.get('query')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
