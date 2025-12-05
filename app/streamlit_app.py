# app/streamlit_app.py

from pathlib import Path
import sys

import pandas as pd
import streamlit as st

# Make the src/ folder importable
project_root = Path(__file__).resolve().parents[1]
src_path = project_root / "src"
sys.path.append(str(src_path))

from load_data import load_orders
import metrics
from scenarios import (
    revenue_with_conversion_uplift,
    revenue_with_aov_uplift,
)


# ------------- Helper functions ------------- #

def load_sample_data() -> pd.DataFrame:
    """
    Load the sample CSV from data/raw using the existing load_orders function.
    """
    csv_path = project_root / "data" / "raw" / "ecommerce_sample.csv"
    return load_orders(csv_path)


def load_uploaded_data(uploaded_file) -> pd.DataFrame:
    """
    Load and clean an uploaded CSV file.

    Expected columns:
    - order_id
    - order_date
    - customer_id
    - channel
    - product
    - quantity
    - unit_price
    - order_status
    """
    df = pd.read_csv(uploaded_file)

    # Mirror the logic from load_orders.py
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["revenue"] = df["quantity"] * df["unit_price"]
    df = df[df["order_status"] == "Completed"].copy()

    return df


# ------------- Streamlit UI ------------- #

st.set_page_config(
    page_title="Analytics & ROI Dashboard",
    layout="wide",
)

st.title("E-commerce Analytics & ROI Dashboard")
st.write(
    "Analyze order data, calculate key KPIs, and model the impact of "
    "conversion and AOV improvements on revenue."
)

# Sidebar controls
with st.sidebar:
    st.header("1. Data source")

    data_source = st.radio(
        "Choose data:",
        ["Use sample data", "Upload CSV file"],
    )

    uploaded_file = None
    if data_source == "Upload CSV file":
        uploaded_file = st.file_uploader(
            "Upload a CSV file",
            type=["csv"],
            help=(
                "File must contain columns: order_id, order_date, customer_id, "
                "channel, product, quantity, unit_price, order_status"
            ),
        )

    st.header("2. Scenario settings")

    conv_uplift = st.slider(
        "Conversion uplift (%)",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=1.0,
        help="Simulated improvement in conversion rate.",
    )

    aov_uplift = st.slider(
        "AOV uplift (%)",
        min_value=0.0,
        max_value=50.0,
        value=5.0,
        step=1.0,
        help="Simulated improvement in average order value.",
    )

# Load data based on user choice
if data_source == "Use sample data":
    df = load_sample_data()
else:
    if uploaded_file is not None:
        df = load_uploaded_data(uploaded_file)
    else:
        df = None
        st.warning("Please upload a CSV file to continue.")

if df is not None and not df.empty:
    # Main layout
    st.subheader("Dataset overview")
    st.dataframe(df.head())

    # Baseline KPIs
    baseline_revenue = metrics.total_revenue(df)
    baseline_orders = metrics.total_orders(df)
    baseline_customers = metrics.unique_customers(df)
    baseline_aov = metrics.average_order_value(df)

    st.subheader("Baseline KPIs")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total revenue", f"${baseline_revenue:,.2f}")
    col2.metric("Total orders", f"{baseline_orders}")
    col3.metric("Unique customers", f"{baseline_customers}")
    col4.metric("Average order value", f"${baseline_aov:,.2f}")

    # Revenue breakdowns
    st.subheader("Revenue breakdowns")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("**Revenue by channel**")
        rev_by_channel = metrics.revenue_by_channel(df)
        st.bar_chart(rev_by_channel)

    with col_right:
        st.markdown("**Revenue by month**")
        rev_by_month = metrics.revenue_by_month(df)
        # Convert PeriodIndex to string for plotting
        rev_by_month.index = rev_by_month.index.astype(str)
        st.line_chart(rev_by_month)

    # Scenario modeling
    st.subheader("Scenario modeling")

    revenue_conv_up = revenue_with_conversion_uplift(baseline_revenue, conv_uplift)
    revenue_aov_up = revenue_with_aov_uplift(baseline_revenue, aov_uplift)

    incremental_conv = revenue_conv_up - baseline_revenue
    incremental_aov = revenue_aov_up - baseline_revenue

    col_s1, col_s2, col_s3 = st.columns(3)

    col_s1.metric(
        "Baseline revenue",
        f"${baseline_revenue:,.2f}",
    )
    col_s2.metric(
        f"Revenue with +{conv_uplift:.0f}% conversion",
        f"${revenue_conv_up:,.2f}",
        f"+${incremental_conv:,.2f}",
    )
    col_s3.metric(
        f"Revenue with +{aov_uplift:.0f}% AOV",
        f"${revenue_aov_up:,.2f}",
        f"+${incremental_aov:,.2f}",
    )

    st.markdown(
        "These scenarios assume revenue scales linearly with conversion and AOV. "
        "In a production environment, you could tie this to real traffic and funnel data."
    )

else:
    st.info("No data available yet. Use the sample data or upload a CSV to begin.")
