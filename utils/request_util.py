import json
import os
import requests
from utils.config import BASE_URL, API_TIMEOUT

def get_events_by_slug(slug: str):
    """Fetch event data from Polymarket API by slug."""
    url = f"{BASE_URL}/events/slug/{slug}"
    response = requests.get(url, timeout=API_TIMEOUT)
    response.raise_for_status()
    return response.json()


def get_markets():
    """Fetch all markets from Polymarket API."""
    url = f"{BASE_URL}/events?order=id&ascending=false&limit=1000000&offset=0"
    response = requests.get(url, timeout=API_TIMEOUT)
    response.raise_for_status()
    return response.json()


def fetch_all_markets():
    all_markets = []
    limit = 500
    offset = 0

    while True:
        print(f"Fetching markets: offset={offset}, limit={limit}")
        resp = requests.get(
            f"{BASE_URL}/events",
            params={
                "order": "id",
                "ascending": "true",
                "limit": limit,
                "offset": offset,
            },
            timeout=20
        )
        resp.raise_for_status()
        data = resp.json()

        if not data:
            break
        print(f"Fetched new {len(data)} markets, total {len(all_markets) + len(data)}")

        all_markets.extend(data)
        offset += limit

    return all_markets


def save_cache(data):
    os.makedirs("cache", exist_ok=True)
    with open("cache/markets.json", "w", encoding="utf-8") as f:
        json.dump(data, f)