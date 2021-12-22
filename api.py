import json
import requests

API_BASEURL = "https://xyz.execute-api.eu-central-1.amazonaws.com/dev"

def api_wave_info(wave: str):

    url = f"{API_BASEURL}/riverwaves/{wave}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers, timeout=30)

    return json.loads(response.content)
