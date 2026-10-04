-- Step 1: Preview raw sales data and compute line-item amounts
SELECT 
    InvoiceNo, 
    StockCode, 
    Quantity, 
    UnitPrice,
    (Quantity * UnitPrice) AS AMOUNT
FROM `Sales.sale`;

-- Step 2: Aggregate total sales and item counts per invoice
CREATE OR REPLACE TABLE `Sales.bills` AS
WITH bills AS (
    SELECT 
        InvoiceNo,
        (Quantity * UnitPrice) AS AMOUNT
    FROM `Sales.sale`
)
SELECT
    InvoiceNo, 
    ROUND(SUM(AMOUNT), 2) AS total, 
    COUNT(*) AS counts
FROM bills
GROUP BY InvoiceNo;
