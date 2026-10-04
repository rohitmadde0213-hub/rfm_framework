# PySpark RFM Customer Segmentation & Analytics

An end-to-end customer segmentation framework built using PySpark SQL and Python[cite: 1]. Computes Recency, Frequency, and Monetary (RFM) metrics, applies quantile scoring, classifies users into marketing tiers, and visualizes insights using Seaborn and Matplotlib[cite: 1].

## Features
* **Big Data Processing:** Uses PySpark DataFrames and temporary SQL views for transactional aggregation[cite: 1].
* **RFM Calculation:** Computes customer recency, frequency, and monetary values via CTEs and window functions[cite: 1].
* **Quantile Scoring:** Implements Spark's `approx_percentile` to assign behavioral scores (1–5)[cite: 1].
* **Segmentation & Visualization:** Classifies customers into distinct marketing segments and plots insights using correlation heatmaps and bar charts[cite: 1].

## Tech Stack
* PySpark / Spark SQL[cite: 1]
* Python (Pandas)[cite: 1]
* Matplotlib / Seaborn[cite: 1]
