# Example configuration for Polymarket Odds Tracker

BASE_URL="https://gamma-api.polymarket.com"
# Data directory for CSV output files
DATA_DIR="output"

# Program 1: Real-time Odds Tracker
# Comma-separated list of event slugs to track
# Example event slugs - replace with actual Polymarket event slugs
REALTIME_EVENTS="jerome-powell-out-as-fed-chair-by,khamenei-out-as-supreme-leader-of-iran-by-january-31"

# Poll interval in seconds (default: 5)
REALTIME_POLL_INTERVAL=5

# Program 2: Market Scanner
# Scan interval in seconds (default: 600 = 10 minutes)
SCANNER_POLL_INTERVAL=600

# API timeout in seconds (default: 10)
API_TIMEOUT=10
