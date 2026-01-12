"""Program 1: Real-time odds tracker.

Polls selected Polymarket event URLs every 1 second and appends
real-time odds ("chance") to CSV.
"""

import json
import time
import requests
import sys
from utils.config import REALTIME_EVENTS, REALTIME_POLL_INTERVAL, SCANNER_POLL_INTERVAL, API_TIMEOUT


def track_event_odds(event_slug: str) -> None:
    """Track odds for a single event and write to CSV.
    
    Args:
        event_slug: Event slug to track
    """
    # event = client.get_event(event_slug)
    print(f"\nFetching odds for event: {event_slug}")
    url = f"https://gamma-api.polymarket.com/events/slug/{event_slug}"

    r = requests.get(url)
    r.raise_for_status()
    event = r.json()

    if not event:
        print(f"Could not fetch event: {event_slug}")
        return
    
    # Get markets associated with this event
    market_id = event.get("id", "")
    market_title = event.get("title", "N/A")
    markets = event.get("markets", [])
    
    for submarket in markets:
        submarket_id = submarket.get("id", "")
        submarket_title = submarket.get("groupItemTitle") or "No Submarket"
        oods = submarket.get("outcomePrices", "[]")
        oods = json.loads(oods)
        first = float(oods[0])

        percentage = round(first * 100) 
        print(f"Market ID: {market_id}, Market Title: {market_title}, Submarket ID: {submarket_id}, Submarket Title: {submarket_title} (ID: {submarket_id}), Odds: {percentage:.2f}%")

def main():
    """Main entry point for real-time odds tracker."""
    print("=== Polymarket Real-Time Odds Tracker ===")
    
    # event_slugs = Config.get_realtime_events()
    event_slugs = REALTIME_EVENTS.split(",")

    try:
        while True:
            for event_slug in event_slugs:
                try:
                    track_event_odds(event_slug)
                except Exception as e:
                    print(f"Error tracking {event_slug}: {e}")
            
            time.sleep(REALTIME_POLL_INTERVAL)
    
    except KeyboardInterrupt:
        print("Stopping tracker...")
    finally:
        print("Tracker stopped.")


if __name__ == "__main__":
    main()
