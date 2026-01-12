# polymarket-data-export
Export polymarket data
## Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## Program Usage

### Program 1: Real-Time Odds Tracker
**Purpose:** Track specific events with 5s polling
#### Note: Update slugs list under /utils/config.py to your targetted slug, separated by comma(,)

```bash
# Run
python track_realtime_odds.py
```

**Output:** `output/realtime_odds.csv`

### Program 2: Market Scanner  
**Purpose:** Scan all markets every 10 minutes

```bash
# Run
python market_scanner.py
```

**Outputs:**
- `data/market_list.csv` - All market list


### Program 3: Historical data
**Purpose:** Get all historical data
On progress