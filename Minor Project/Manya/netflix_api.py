# netflix_api.py

import http.client
import json
from config import NETFLIX_API_KEY

def get_season_episodes(season_id, offset=0, limit=25, language="en"):
    conn = http.client.HTTPSConnection("netflix54.p.rapidapi.com")
    
    headers = {
        "x-rapidapi-key": NETFLIX_API_KEY,
        "x-rapidapi-host": "netflix54.p.rapidapi.com"
    }
    
    url = f"/season/episodes?ids={season_id}&offset={offset}&limit={limit}&lang={language}"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    
    try:
        episodes = json.loads(data.decode("utf-8"))
        return episodes
    except json.JSONDecodeError:
        print("Failed to parse JSON response")
        return None
