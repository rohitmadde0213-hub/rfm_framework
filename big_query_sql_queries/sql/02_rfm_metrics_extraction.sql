-- Step 3: Extract Recency, Frequency, and Monetary metrics per customer
CREATE OR REPLACE TABLE `Sales.rfm` AS
WITH cte AS (
    SELECT 
        s.CustomerID, 
        DATE(MAX(s.InvoiceDate)) AS last_purchase_date,
        DATE(MIN(s.InvoiceDate)) AS first_purchase_date,
        COUNT(DISTINCT s.InvoiceNo) AS num_purchase,      
        ROUND(SUM(b.total), 2) AS monetary 
    FROM `Sales.sale` s
    LEFT JOIN `Sales.bills` b
        ON s.InvoiceNo = b.InvoiceNo
    GROUP BY s.CustomerID
)
SELECT 
    *,
    DATE_DIFF(reference_date, last_purchase_date, DAY) AS recency,
    ROUND(num_purchase / month_cust, 2) AS frequency 
FROM (
    SELECT 
        *, 
        MAX(last_purchase_date) OVER () + 1 AS reference_date,
        DATE_DIFF(last_purchase_date, first_purchase_date, MONTH) + 1 AS month_cust
    FROM cte
);
