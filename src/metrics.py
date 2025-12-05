# src/metrics.py

import pandas as pd


def total_revenue(df: pd.DataFrame) -> float:
    """
    Sum of revenue across all orders.
    """
    return float(df["revenue"].sum())


def total_orders(df: pd.DataFrame) -> int:
    """
    Count of unique orders.
    """
    # assuming order_id is unique per order
    return int(df["order_id"].nunique())


def unique_customers(df: pd.DataFrame) -> int:
    """
    Count of unique customers.
    """
    return int(df["customer_id"].nunique())


def average_order_value(df: pd.DataFrame) -> float:
    """
    Average order value (AOV) = total revenue / total orders.
    """
    orders = total_orders(df)
    if orders == 0:
        return 0.0
    return float(total_revenue(df) / orders)


def revenue_by_channel(df: pd.DataFrame) -> pd.Series:
    """
    Total revenue grouped by sales channel.
    """
    return (
        df.groupby("channel")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def revenue_by_month(df: pd.DataFrame) -> pd.Series:
    """
    Total revenue grouped by year-month (e.g., 2024-01, 2024-02).
    """
    tmp = df.copy()
    tmp["year_month"] = tmp["order_date"].dt.to_period("M")
    return (
        tmp.groupby("year_month")["revenue"]
        .sum()
        .sort_index()
    )
