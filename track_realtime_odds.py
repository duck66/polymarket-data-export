"""Program 1: Real-time odds tracker.

Polls selected Polymarket event URLs every 1 second and appends
real-time odds ("chance") to CSV.
"""

import json
import time
import sys
from utils.request_util import get_events_by_slug
from utils.csv_util import append_csv, now_central
from utils.config import REALTIME_EVENTS, REALTIME_POLL_INTERVAL


def track_event_odds(event_slug: str) -> None:
    """Track odds for a single event and write to CSV.
    
    Args:
        event_slug: Event slug to track
    """
    
    event = get_events_by_slug(event_slug)

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

        # Chance/Odds stored on first index of outcomePrices value
        oods = submarket.get("outcomePrices", "[]")
        oods = json.loads(oods)
        first = float(oods[0])

        # ROunded so it have same value as the one listed on Polymarket site
        percentage = round(first * 100)
        append_csv([{
            "market_id": market_id,
            "market_title": market_title,
            "submarket_id": submarket_id,
            "submarket_title": submarket_title,
            "time": now_central(),
            "chance": f"{percentage}%"
        }])
        print(f"Market ID: {market_id}, Market Title: {market_title}, Submarket ID: {submarket_id}, Submarket Title: {submarket_title} (ID: {submarket_id}), Odds: {percentage:.2f}%")

def main():
    """Main entry point for real-time odds tracker."""
    print("=== Polymarket Real-Time Odds Tracker ===")
    
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
