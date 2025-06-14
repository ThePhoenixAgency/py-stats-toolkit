import os
import json
from datetime import datetime

STRATEGY_DIR = "."
STRATEGY_PREFIX = "strategie_euromillions_"
STRATEGY_EXTENSION = ".json"

def get_latest_strategy_file():
    files = [
        f for f in os.listdir(STRATEGY_DIR)
        if f.startswith(STRATEGY_PREFIX) and f.endswith(STRATEGY_EXTENSION)
    ]
    if not files:
        return None
    latest = max(files, key=lambda f: datetime.strptime(f[len(STRATEGY_PREFIX):-len(STRATEGY_EXTENSION)], "%Y%m%d"))
    return os.path.join(STRATEGY_DIR, latest)

def load_latest_strategy():
    strategy_file = get_latest_strategy_file()
    if not strategy_file:
        return None, "Aucune stratégie trouvée."
    with open(strategy_file, "r") as f:
        return json.load(f), None