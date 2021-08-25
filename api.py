import requests
import json

API_BASEURL = "https://xyz132.eu-central-1.amazonaws.com/prod"

def api_latest(wave: str):

    url = f"{API_BASEURL}/riverwaves/{wave}/latest"
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request('GET', url, headers=headers, timeout=30)
        return json.loads(response.content)

    except:
        return {'water_temp': 'ERR', 'datetime': 'ERR',
                'water_level': 'ERR', 'water_runoff': 'ERR'}