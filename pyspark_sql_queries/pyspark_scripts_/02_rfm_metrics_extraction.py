# Extract Recency, Frequency, and Monetary metrics per customer
rfm = spark.sql("""
    WITH cte AS (
        SELECT 
            s.CustomerID, 
            TO_DATE(MAX(s.InvoiceDate)) AS last_purchase_date,
            TO_DATE(MIN(s.InvoiceDate)) AS first_purchase_date,
            COUNT(DISTINCT s.InvoiceNo) AS num_purchase,      
            ROUND(SUM(b.total), 2) AS monetary 
        FROM sales s
        LEFT JOIN bills b
            ON s.InvoiceNo = b.InvoiceNo
        GROUP BY s.CustomerID
    )
    SELECT 
        CustomerID,
        last_purchase_date,
        first_purchase_date,
        num_purchase,
        monetary,
        reference_date,
        DATEDIFF(reference_date, last_purchase_date) AS recency,
        ROUND(num_purchase / month_cust, 2) AS frequency 
    FROM (
        SELECT 
            *, 
            DATE_ADD(MAX(last_purchase_date) OVER (), 1) AS reference_date,
            GREATEST(CAST(MONTHS_BETWEEN(last_purchase_date, first_purchase_date) AS INT), 0) + 1 AS month_cust
        FROM cte
    )
""")

rfm.createOrReplaceTempView("rfm")
rfm.show()
