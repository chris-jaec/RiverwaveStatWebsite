import json

import requests

API_ID = "api_id"
API_KEY = "api_secret"
API_STAGE = "prod"
API_REGION = "eu-central-1"
API_BASEURL = f"https://{API_ID}.execute-api.{API_REGION}.amazonaws.com/{API_STAGE}"

def api_wave_info(wave: str):
    url = f"{API_BASEURL}/riverwaves/{wave}"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }

    response = requests.get(url, headers=headers, timeout=30)

    return json.loads(response.content)


def api_wave_overview():
    url = f"{API_BASEURL}/riverwaves/"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }

    response = requests.get(url, headers=headers, timeout=30)

    return json.loads(response.content)
