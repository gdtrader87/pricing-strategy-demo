# Deriving Pricing Strategies from Enterprise Dashboards

These Adobe enterprise dashboards (BOQ Historical Pipeline, Customer Success, Customer 360, CCE Usage and others) capture rich B2C customer‑journey metrics across product families (CCE, DCE, CCE Pro, Stock, Sign, Substance and more). They provide insight into pipeline, activation and utilization that can inform dynamic pricing models and experimentation.

## Key Metrics Observed

1. **Pipeline Coverage (BOQ) by Geography, Solution and Sales Motion** – The BOQ historical pipeline dashboard shows quarterly averages and gaps between pipe actual and quota‑based revenue forecast (QRF) across regions, products (e.g., Acrobat, CCE Pro, Sign, Stock) and sales motions (Growth on renewal, New, True up). By tracking how actual pipeline coverage deviates from QRF attainment and by segmenting by vertical or sales motion, we can identify where price sensitivity might be higher or lower.

2. **QRF Attainment and Gap Analysis** – The spreadsheet snapshots highlight QRF attainment percentages and pipe gaps for various business units. A high pipe gap (e.g., 1.3× ratio indicating a shortage) suggests that either volume or price needs to increase. Combining this with pipeline trends helps determine whether a price decrease could stimulate demand or if demand is inelastic.

3. **License Activation and Usage Metrics (QAL, MAL, RMAL)** – Dashboards such as Customer 360 – CCE Usage display assignment and activation rates (assigned vs. entitled seats, activated vs. assigned) and week‑over‑week changes across offerings. Metrics like QAL (Qualified Activation Level), MAL (Manual Activation Level) and RMAL (Recurring Manual Activation Level) capture how many seats are entitled, assigned and activated over time. Low assignment or activation rates can signal that the current pricing or packaging is not aligned with customer value perception. Monitoring trends across products (Photoshop, Lightroom, Premiere Pro, etc.) reveals which applications drive stickiness and where bundling or promotional pricing could improve utilization.

4. **Customer Segmentation by Parent and Child Companies** – Customer 360 dashboards provide hierarchy filters for parent, sub and child geos. Segmenting customers by parent companies (e.g., General Mills, Disney, Toyota, General Motors, Microsoft) and their subsidiaries allows the business to tailor pricing and engagement strategies. A large parent company may tolerate higher prices while smaller subsidiaries might be more price sensitive. Tracking pipeline, activation and support metrics across this hierarchy helps calibrate segment‑specific pricing.

5. **Support Tickets and Customer Engagement** – Metrics such as number of customer engagements by date, open and closed support cases, and customer satisfaction/effort scores provide context for willingness to pay. A surge in support tickets for a specific product or segment may indicate usability issues; these customers may require increased value or training rather than price increases. Conversely, high engagement and satisfaction may correlate with higher price tolerance.

6. **Account Health and Competitive Landscape** – Customer 360 dashboards show account and solution health indicators (Green, Yellow, Red) alongside competitor presence. Accounts flagged as “at risk” with low health scores or heavy competitor penetration may require targeted discounting or value‑added pricing to prevent churn. Competitive landscape tables show competitor products by solution, which can help benchmark pricing and position premium tiers.

## Pricing Strategy Recommendations

Based on these dashboards, a pricing strategy could include:

1. **Segmentation‑Based Dynamic Pricing** – Cluster customers by region, vertical, sales motion, parent company hierarchy and usage patterns, then compute price elasticity within each segment using historical pipeline and QRF attainment data. For instance, BOQ coverage by solution indicates that Stock may have a sudden spike in demand; a dynamic pricing model could temporarily raise price in that segment while maintaining competitive pricing for Acrobat and Sign. Similarly, large enterprise parents like Microsoft may sustain premium pricing while smaller subsidiaries may require discounts to drive adoption.

2. **Elasticity‑Driven Discounts and Promotions** – Use pipe actual vs. pipe gap data to identify segments with elastic demand. If pipe gaps are consistently negative for a product like CCE Pro in certain geographies or sub‑companies, implement promotional pricing (e.g., limited‑time discounts, bundle offers or tiered pricing) to stimulate demand and close the gap. Combine this with activation metrics to ensure discounts drive real usage rather than unactivated entitlement.

3. **Retention‑Focused Pricing** – Cross‑reference activation/assignment rates and support‑ticket volume with account health. For customers with high entitlement but low activation or high RMAL, offer usage‑based or consumption pricing tiers to lower upfront cost while incentivizing adoption. For accounts at risk (red/yellow) or those filing many support tickets, introduce loyalty pricing, training packages or add‑on services to reduce churn.

4. **Experimentation and A/B Testing** – Leverage the dashboards’ time‑series views to design experiments on price changes. For example, adjust pricing for Stock in a specific vertical and monitor changes in pipeline coverage, QRF attainment, activation rates and support‑ticket volume versus a control group. Use statistical significance testing to evaluate the impact and iterate.

5. **Value‑Based Bundling** – The Customer 360 – CCE Usage by application dashboard reveals which apps drive activation and adoption. Bundle high‑value apps (Photoshop, Premiere) with lower‑utilization apps (Character Animator, Dreamweaver) at a combined price that enhances perceived value while increasing overall revenue. For segments with high support cost, bundle support services into premium tiers.

## How to Incorporate into Your Portfolio

To demonstrate pricing‑strategy expertise:

- **Narrative** – Include a write‑up in your GitHub repository summarizing the above insights and how you would translate them into pricing experiments. Highlight your ability to interpret pipeline, hierarchy and usage metrics to inform data‑driven pricing. Showcase segmentation by parent/child companies and how support tickets influence pricing decisions.
- **Code** – Complement the narrative with the Python elasticity demo (`pricing_elasticity.py`) and the ETL pipeline (`etl_pipeline.py`) that generates synthetic pipeline, usage and support data for parent and sub companies. Consider extending the elasticity script to load anonymized pipeline data (e.g., pipe actual, QRF attainment, activation rates) to estimate demand curves for different segments.
- **Visuals** – Use Matplotlib or Tableau Public to recreate charts similar to the dashboards (without sensitive data) to visualize the impact of different pricing scenarios. Include line charts for pipeline coverage vs. QRF attainment, bar charts for activation rates across parent companies, and scatter plots for price vs. revenue.

This approach demonstrates your capability to reverse engineer complex dashboards and derive actionable pricing strategies from B2C enterprise data, aligning with Earnest’s requirement for ownership of dynamic pricing models, price elasticity analysis and experimentation initiatives.
