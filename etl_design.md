# ETL Pipeline Design

This document outlines a high‑level ETL (extract–transform–load) pipeline designed to power dashboards similar to Adobe’s BOQ Historical Pipeline, Customer Success and Customer 360 views.

## Data Sources

- **Sales Pipeline** – Records from the CRM (e.g., Salesforce) capturing opportunities, deal stage, region, solution, sales motion and QRF (quota‑based revenue forecast). Fields include Opportunity ID, Account ID, Stage, Fiscal Week, Pipe Actual $, QRF, Sales Motion (Growth on renewal, New, True up), etc.
- **Customer Hierarchy** – Parent/child company mapping that links accounts to parent organisations and allows segmentation by region, vertical and customer type.
- **Licensing & Usage Analytics** – Tables with seat entitlements, assignment and activation events per product (CCE, DCE, CCE Pro, Stock, Sign, etc.), week‑over‑week activation counts (QAL, MAL, RMAL) and utilisation percentages.
- **Support & Engagement** – Support ticket logs and customer engagement activities with timestamps, categories and resolutions; metrics used to infer adoption and satisfaction levels.
- **Product Catalogue & Pricing** – Lookup tables mapping solutions to product families, list price and discount bands.

## Transformation Steps

1. **Normalize and Clean** – Standardise field names, fix missing or inconsistent values (e.g., unify region codes, normalise fiscal week).
2. **Join Hierarchies** – Merge pipeline data with the customer hierarchy to attach parent/child relationships and segment by GEO, vertical and sales motion.
3. **Compute Pipeline Metrics** – For each combination of geography, solution and sales motion:
   - Calculate pipeline coverage: `Pipe Actual / QRF`.
   - Determine pipe gap and gap ratio: `QRF - Pipe Actual` and `(QRF - Pipe Actual) / QRF`.
   - Aggregate weekly and quarterly pipeline to compute historical BOQ averages.
4. **Aggregate Activation & Usage** – For each account and product family:
   - Count entitled, assigned and activated seats; compute assignment and activation rates.
   - Generate week‑over‑week counts of QAL (quality activation), MAL (medium activation) and RMAL (reduced activation) to track adoption trends.
   - Join support tickets and engagement activities to enrich with adoption context.
5. **Customer Health & Segmentation** – Derive health scores (Green, Yellow, Red) based on activation rates, pipe coverage, support ticket volume and competitive presence. Group by parent/child company to identify at‑risk segments.
6. **Load to Analytics Warehouse** – Write the transformed tables (pipeline metrics, activation metrics, health segments) into a data warehouse or export as CSV files. Use these data sets to power dashboards and analytics tools such as Power BI or Tableau.

## Usage Notes

This pipeline design provides the foundation for dashboards that track pipeline coverage, attainment, activation and usage, enabling pricing strategies based on customer adoption. By combining pipeline metrics with usage and support data, you can compute price elasticity within segments and support dynamic pricing and discount programs.
