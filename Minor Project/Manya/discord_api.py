# discord_api.py

import requests
from config import DISCORD_API_KEY

def send_discord_message(channel_id, message):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {DISCORD_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": message
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code == 200
