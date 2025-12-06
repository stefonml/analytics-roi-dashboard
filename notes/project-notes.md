# Project 1 – Analytics & ROI Dashboard

## One-line summary
E-commerce analytics toolkit that calculates KPIs and models the revenue impact of conversion and AOV improvements.

## Problem Statement
- Small businesses don't always understand the impact of improving conversion or AOV on revenue.
- Need a simple, transparent toolkit to model "what-if" scenarios.

## Goals
- Load order data from CSV.
- Compute: total revenue, orders, customers, AOV.
- Visualize revenue by channel and month.
- Show the revenue impact of:
  - +X% conversion
  - +Y% AOV

## Tech Stack
- Python
- Pandas
- Matplotlib
- Jupyter
- Git, GitHub, VS Code

## Tasks / To-Do
- [x] Set up project structure in VS Code
- [x] Connect repo to GitHub
- [x] Implement load_data.py
- [x] Implement metrics.py
- [x] Implement scenarios.py
- [x] Implement visualize.py
- [x] Create Jupyter notebook (01_exploration.ipynb)
- [x] Take screenshots for docs/screenshots
- [x] Polish README.md0
- [x] Add streamlit ui for analytics and ROI dashboard
## Notes / Decisions
- Revenue = quantity * unit_price for completed orders only.
- Start with simple, linear scenario modeling; refine later.
