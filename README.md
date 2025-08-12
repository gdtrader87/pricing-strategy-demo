# Pricing Strategy & ETL Demo

This repository demonstrates how to reverse‑engineer a data pipeline and pricing strategy from enterprise dashboards. It includes sample code and documentation inspired by Adobe's pipeline and customer‑success dashboards, but using synthetic data.

## Contents

- `etl_design.md` – documentation outlining the data sources, transformations, metrics and load steps behind the dashboards. It shows how pipeline, forecast and usage data are combined to compute key metrics (pipeline coverage, QRF attainment, assignment/activation rates) and support a Customer 360 view.
- `etl_pipeline.py` – example Python script that simulates an ETL pipeline: extracts mock pipeline and usage data, transforms it to compute metrics, and loads the results into a CSV.
- `pricing_elasticity.py` – a Python script that creates a simple price/quantity dataset, estimates a demand curve and price elasticity, computes an optimal price and plots revenue versus price. This demonstrates dynamic pricing analysis and experimentation.
- `pricing_strategy_from_dashboards.md` – a write‑up explaining how to derive segmentation‑based pricing strategies from the observed dashboard metrics.

## How to use

1. Clone or download this repository.
2. Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib
```

3. Run `etl_pipeline.py` to generate a transformed dataset:

```bash
python etl_pipeline.py
```

4. Run `pricing_elasticity.py` to perform the pricing analysis:

```bash
python pricing_elasticity.py
```

The scripts use synthetic data; feel free to replace them with your own anonymized pipeline and usage data to replicate enterprise dashboards and test different pricing scenarios.
