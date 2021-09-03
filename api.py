import json
import requests_cache

API_BASEURL = "https://xyz.execute-api.eu-central-1.amazonaws.com/dev"

SESSION = requests_cache.CachedSession(expire_after=120, backend="memory")

def api_wave_info(wave: str):

    url = f"{API_BASEURL}/riverwaves/{wave}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = SESSION.get(url, headers=headers, timeout=30)

    return json.loads(response.content)