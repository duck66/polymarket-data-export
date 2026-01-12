import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from utils.config import DATA_DIR, TIMEZONE, DATE_FORMAT

REALTIME_ODDS_FIELDS = [
    "market_id",
    "market_title",
    "submarket_id",
    "submarket_title",
    "time",
    "chance"
]

MARKET_LIST_FIELDS = [
    "market_id",
    "market_title",
    "submarket_id",
    "submarket_title",
    "registered",
    "resolved",
    "volume"
]


CSV_FILE = f"{DATA_DIR}/realtime_odds.csv"

def append_csv(program, rows):
    """Append rows to CSV file."""

    csv_file = f"{DATA_DIR}/{program}.csv"

    field_mapping = {
        "realtime_odds": REALTIME_ODDS_FIELDS,
        "market_list": MARKET_LIST_FIELDS,
    }

    fields = field_mapping.get(program)    

    file_exists = os.path.isfile(csv_file)

    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerows(rows)


def now_central():
    """Get current time in Central timezone formatted as string."""
    return datetime.now(ZoneInfo(TIMEZONE)).strftime(
        DATE_FORMAT
    )


def format_central(iso_str: str) -> str:
    """Format ISO datetime string to Central timezone."""
    if not iso_str:
        return ""

    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    dt_central = dt.astimezone(ZoneInfo(TIMEZONE))

    return dt_central.strftime(DATE_FORMAT)
