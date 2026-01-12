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
    url = f"{BASE_URL}/events?limit=100&offset=0&ascending=false&order=id"
    response = requests.get(url, timeout=API_TIMEOUT)
    response.raise_for_status()
    return response.json()