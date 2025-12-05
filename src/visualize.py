# src/visualize.py

from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd

import metrics  # relies on src/ being on sys.path


def plot_revenue_by_channel(df: pd.DataFrame, show: bool = True, save_path: Optional[str] = None):
    """
    Bar chart: revenue by channel.
    """
    series = metrics.revenue_by_channel(df)

    plt.figure()
    series.plot(kind="bar")
    plt.title("Revenue by Channel")
    plt.xlabel("Channel")
    plt.ylabel("Revenue")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_revenue_by_month(df: pd.DataFrame, show: bool = True, save_path: Optional[str] = None):
    """
    Line chart: revenue by year-month.
    """
    series = metrics.revenue_by_month(df)
    # Convert PeriodIndex to string for plotting
    series.index = series.index.astype(str)

    plt.figure()
    series.plot(kind="line", marker="o")
    plt.title("Revenue by Month")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()
