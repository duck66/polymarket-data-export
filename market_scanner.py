"""Program 2: Market Scanner.

Polls selected Polymarket event URLs every 10 minutes and appends
market data to CSV.
"""
import time
from utils.config import SCANNER_POLL_INTERVAL
from utils.request_util import get_markets
from utils.csv_util import append_csv, format_central


def get_market_data():
    """Fetch and process market data for all selected events."""
    event_list = get_markets()
    
    if not event_list:
        print(f"Could not fetch event")
        return
    for event in event_list:
    
        # Process market data as needed
        market_id = event.get("id", "")
        market_title = event.get("title", "N/A")
        markets = event.get("markets", [])
        
        for submarket in markets:
            submarket_id = submarket.get("id", "")
            submarket_title = submarket.get("groupItemTitle") or "No Submarket"
            volume = submarket.get("volume", "0.0")
            volume = f"${int(float(volume))}"
            registered = event.get("startDate", "")

            # Date format inconsisten, wrap in try catch to avoid raise
            try:
                registered_fmt = format_central(registered)
            except Exception:
                registered_fmt = registered
            resolved = event.get("endDate", "")
            try:
                resolved_fmt = format_central(resolved)
            except Exception:
                resolved_fmt = resolved

            append_csv("market_list", [{
                "market_id": market_id,
                "market_title": market_title,
                "submarket_id": submarket_id,
                "submarket_title": submarket_title,
                "registered": registered_fmt,
                "resolved": resolved_fmt,
                "volume": volume
            }])
            
            print(f"[Scanner] Market ID: {market_id}, Market Title: {market_title}, Submarket ID: {submarket_id}, Submarket Title: {submarket_title}, Registered: {registered_fmt}, Resolved: {resolved_fmt}, Volume: {volume}")


def main():
    """Main entry point for market scanner."""
    print("=== Polymarket Market Scanner ===")

    try:
        while True:
            try:
                get_market_data()
            except Exception as e:
                print(f"Error getting market data: {e}")
            time.sleep(SCANNER_POLL_INTERVAL)
    
    except KeyboardInterrupt:
        print("Stopping scanner...")
    finally:
        print("Scanner stopped.")


if __name__ == "__main__":
    main()
