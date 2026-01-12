import requests
from utils.config import BASE_URL, API_TIMEOUT

def get_events_by_slug(slug: str):
    """Fetch event data from Polymarket API by slug."""
    url = f"{BASE_URL}/events/slug/{slug}"
    response = requests.get(url, timeout=API_TIMEOUT)
    response.raise_for_status()
    return response.json()
