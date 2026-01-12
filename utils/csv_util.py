import csv
import os

from utils.config import DATA_DIR

CSV_FIELDS = [
    "market_id",
    "market_title",
    "submarket_id",
    "submarket_title",
    "chance",
]

CSV_FILE = "output/realtime_odds.csv"

def append_csv(rows):
    file_exists = os.path.isfile(CSV_FILE)

    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerows(rows)
