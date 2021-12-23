import json

import requests

API_ID = "238wsp254h"
API_STAGE = "dev"
API_REGION = "eu-central-1"
API_BASEURL = f"https://{API_ID}.execute-api.{API_REGION}.amazonaws.com/{API_STAGE}"


def api_wave_info(wave: str):
    url = f"{API_BASEURL}/riverwaves/{wave}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers, timeout=30)

    return json.loads(response.content)
