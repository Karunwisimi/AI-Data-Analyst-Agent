from pathlib import Path
import pandas as pd


DATA_DIR = Path("Data")


def load_transaction_chunks(chunksize=100_000):
    files = sorted(DATA_DIR.glob("transactions_part_*.csv"))

    if not files:
        raise FileNotFoundError(
            f"No transaction CSV files found in {DATA_DIR.resolve()}"
        )

    for file in files:
        for chunk in pd.read_csv(file, chunksize=chunksize):
            yield chunk