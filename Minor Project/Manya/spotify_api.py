# spotify_api.py

import requests
from config import SPOTIFY_API_KEY

def get_spotify_data(endpoint, params=None):
    url = f"https://api.spotify.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {SPOTIFY_API_KEY}"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None
