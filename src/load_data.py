# src/load_data.py

from pathlib import Path
from typing import Union

import pandas as pd


def load_orders(csv_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load e-commerce orders from a CSV file and perform minimal cleaning.

    Steps:
    - Read the CSV.
    - Parse order_date as datetime.
    - Compute revenue = quantity * unit_price.
    - Filter to order_status == 'Completed'.

    :param csv_path: Path to the CSV file.
    :return: Cleaned pandas DataFrame.
    """
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    df = pd.read_csv(csv_path)

    # Parse dates
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Compute revenue
    df["revenue"] = df["quantity"] * df["unit_price"]

    # Filter completed orders only
    df = df[df["order_status"] == "Completed"].copy()

    return df
