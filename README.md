# shopping-mall-ads-dashboard
Operational marketing dashboard using Kaggle Shopping Mall Paid Search dataset

# Shopping Mall Ads – Paid Search Campaign Analysis

This repo contains the data preparation and analysis code behind my **Shopping Mall Ads Paid Search** dashboard, built in Tableau Public as part of my analytics portfolio.

## Data

- **Source:** [Shopping Mall Ads dataset on Kaggle](<https://www.kaggle.com/datasets/marceaxl82/shopping-mall-paid-search-campaign-dataset/data>)
- **Grain:** Paid search campaign performance by date, device, keyword match type, and theme.
- **Key fields:** impressions, clicks, conversions, revenue, cost, device, theme, match type, date.

## What I did

All of the work in this repo is done in Jupyter notebooks (see `/notebooks`):

1. **Data cleaning**
   - Loaded the raw Kaggle CSV.
   - Standardized column names and date formats.
   - Removed unused fields and handled nulls / inconsistent labels.

2. **Feature engineering**
   - Created derived metrics:
     - CTR = clicks / impressions
     - CPA = cost / conversions
     - P&L = revenue – cost
     - Impression-to-Conversion Rate = conversions / impressions
   - Bucketed data into:
     - **Monthly** time series for trend analysis.
     - **Theme-level** and **device-level** aggregates.

3. **Export for Tableau**
   - Saved a cleaned, aggregated CSV (`/data/processed/shopping_mall_ads_agg.csv`) used to power the Tableau Public dashboard.

## Tableau dashboard

The final dashboard is hosted on Tableau Public:

- **Dashboard:** <https://public.tableau.com/app/profile/dani.valades/viz/ShoppingMallAdsDashboard/Dashboard1?publish=yes>

It shows:
- Top-level KPIs (Revenue, Cost, P&L, Impressions, CTR, CPA, Impression-to-Conversion Rate).
- Breakdowns by campaign theme and device.
- A dual-axis time series of Impressions + CTR and Cost + CPA to show seasonality and efficiency over time.

> **Note:** This campaign is historical, so the dashboard uses a static extract.  
> In a production environment with live spend, I would connect to a warehouse (e.g. Snowflake/BigQuery) and schedule extract refreshes **daily** (and **2–3x per day** during peak periods) to support near–real-time monitoring and optimization.

## Reproducing the analysis

Requirements:

- Python 3.x
- `pandas`, `numpy`, `jupyter`

Steps:

```bash
# clone the repo
git clone <your-repo-url>
cd <your-repo-name>

# optionally create a venv
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt  # if you create one

# launch notebooks
jupyter notebook
