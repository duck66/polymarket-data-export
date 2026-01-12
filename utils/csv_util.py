import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from utils.config import DATA_DIR

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
    return datetime.now(ZoneInfo("America/Chicago")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def format_central(iso_str: str) -> str:
    if not iso_str:
        return ""

    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    dt_central = dt.astimezone(ZoneInfo("America/Chicago"))

    return dt_central.strftime("%Y-%m-%d %H:%M:%S")
