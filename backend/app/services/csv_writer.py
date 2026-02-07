import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/user_inputs.csv")


def write_to_csv(payload: dict):
    try:
        df = pd.DataFrame([payload])
        CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(
            CSV_PATH,
            mode="a" if CSV_PATH.exists() else "w",
            header=not CSV_PATH.exists(),
            index=False,
            encoding="utf-8"
        )
    except Exception as e:
        print(f"CSV write failed: {e}")
