from pathlib import Path

DATA_DIR = Path(__file__).parent

HARD_DEALS = []
with open(DATA_DIR / "hard.txt") as f:
    for line in f:
        HARD_DEALS.append(int(line.strip()))

EASY_DEALS = []
with open(DATA_DIR / "easy.txt") as f:
    for line in f:
        EASY_DEALS.append(int(line.strip()))
