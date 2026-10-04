# 📊 PySpark & BigQuery RFM Customer Segmentation & Analytics

> *Unlocking customer lifetime value through big data processing, behavioral scoring, and actionable segmentation.*

---

## 🌟 Overview
Welcome to the **PySpark & BigQuery RFM Framework**! This repository provides a robust, scalable pipeline for analyzing customer behavior using both **PySpark SQL** and **BigQuery**. By translating raw transactional logs into **Recency, Frequency, and Monetary (RFM)** metrics, this project helps businesses identify high-value buyers, mitigate churn risk, and target marketing campaigns effectively.

---

## ⚙️ Key Features
* **Dual-Platform Support:** Features scalable codebases implemented in both PySpark SQL and BigQuery.
* **Big Data Processing:** Leverages PySpark DataFrames, temporary SQL views, and cloud data warehousing to handle large-scale sales datasets.
* **Advanced RFM Modeling:** Utilizes Common Table Expressions (CTEs), window functions, and date arithmetic to compute accurate customer metrics.
* **Quantile Scoring Engine:** Implements approximate percentile functions to dynamically distribute customers across 1–5 behavioral tiers.
* **Behavioral Segmentation:** Groups users into 11 strategic marketing segments (e.g., *Champions*, *Loyal Customers*, *At Risk*, *Hibernating*).
* **Rich Data Visualization:** Bridges big data outputs with Pandas, Matplotlib, and Seaborn to produce correlation heatmaps and volume-vs-spend bar charts.

---

## 🛠️ Tech Stack & Libraries
* **Big Data / Cloud SQL:** PySpark, Spark SQL, BigQuery, Window Functions, CTEs
* **Data Manipulation:** Python, Pandas
* **Visualization:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebook / Google Colab

---

## 📈 Visualizing Insights
The pipeline processes the data through multiple analytical phases:
1. **Invoice Aggregation:** Calculates item-level and invoice-level totals.
2. **Metric Extraction:** Computes lifetime metrics like `recency`, `frequency`, and `monetary` value per customer.
3. **Scoring & Grouping:** Evaluates quantiles to assign robust performance tiers.
