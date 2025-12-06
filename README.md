# Analytics & ROI Dashboard

An e-commerce analytics toolkit that ingests order data, calculates key KPIs, and models the impact of improving conversion and AOV on revenue.

# Analytics & ROI Dashboard

An e-commerce analytics toolkit and interactive dashboard that ingests order data, calculates key KPIs, and models the revenue impact of conversion and AOV improvements.

Built with Python, Pandas, Matplotlib, and Streamlit.

---

## 1. Problem

Many small businesses and product teams struggle to answer questions like:

- *“What happens to revenue if we improve conversion by 5–10%?”*  
- *“How much upside is there if we increase AOV with bundles or upsells?”*  

Raw order data exists in spreadsheets or exports, but it’s not organized into clear metrics or scenario models that non-technical stakeholders can understand.

---

## 2. Solution

This project provides:

- A **reusable analytics toolkit**:
  - Clean and transform order data from CSV
  - Compute key metrics (revenue, orders, customers, AOV)
  - Break down revenue by channel and by month
- An **interactive Streamlit dashboard**:
  - Upload your own CSV or use sample data
  - View baseline KPIs and revenue breakdowns
  - Use sliders to simulate:
    - Conversion uplift (e.g., +10%)
    - AOV uplift (e.g., +5%)
  - Instantly see the revenue impact

---

## 3. Features

**Data & Metrics**

- Load orders from CSV (sample dataset included)
- Filter to completed orders
- Compute:
  - Total revenue
  - Total orders
  - Unique customers
  - Average order value (AOV)
- Revenue breakdowns:
  - By channel (e.g., Amazon, Direct, Dealer)
  - By month (e.g., 2024-01, 2024-02)

**Scenario Modeling**

- Simulate *conversion uplift* (0–50%)
- Simulate *AOV uplift* (0–50%)
- Show:
  - New projected revenue
  - Incremental revenue vs baseline

**Streamlit UI**

- Sidebar controls for:
  - Data source (sample vs uploaded CSV)
  - Conversion uplift %
  - AOV uplift %
- Main dashboard:
  - Data preview
  - KPI summary tiles
  - Revenue by channel (bar chart)
  - Revenue by month (line chart)
  - Scenario comparison metrics

---

## 4. Screenshots

> Replace these image paths with your actual screenshot files from `docs/screenshots/`.

### Dashboard (overview)

![Streamlit dashboard](docs/screenshots/streamlit_dashboard_full.png)

### Scenario modeling

![Scenario metrics](docs/screenshots/streamlit_scenarios.png)

---

## 5. Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Streamlit, Jupyter  
- **Tools:** VS Code, Git, GitHub  

---

## 6. Project Structure

```text
analytics-roi-dashboard/
  app/
    streamlit_app.py        # Streamlit UI
  data/
    raw/
      ecommerce_sample.csv  # Sample dataset
  docs/
    screenshots/            # Dashboard images for the portfolio
  notebooks/
    01_exploration.ipynb    # Exploration & analysis notebook
  src/
    __init__.py
    load_data.py            # CSV loading & cleaning
    metrics.py              # KPI calculations
    scenarios.py            # Scenario modeling (conversion & AOV uplift)
    visualize.py            # Matplotlib charts (notebook usage)
  requirements.txt
  README.md
