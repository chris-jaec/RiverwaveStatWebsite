import json
import os

import requests

API_ID = os.environ.get("API_ID")
API_STAGE = os.environ.get("STAGE")
API_REGION = os.environ.get("REGION")

API_BASEURL = f"https://{API_ID}.execute-api.{API_REGION}.amazonaws.com/{API_STAGE}"


def api_wave_info(wave: str):
    url = f"{API_BASEURL}/riverwaves/{wave}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers, timeout=30)

    return json.loads(response.content)
