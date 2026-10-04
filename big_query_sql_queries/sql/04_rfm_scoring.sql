-- Step 5: Assign behavioral scores (1-5) based on quantile distributions
CREATE OR REPLACE TABLE `Sales.score` AS
SELECT 
    CustomerID, 
    m_score, 
    f_score, 
    r_score, 
    monetary, 
    frequency, 
    recency, 
    CAST(ROUND((f_score * m_score) / 2.0) AS INT64) AS fm_score
FROM ( 
    SELECT 
        *, 
        CASE 
            WHEN monetary <= m20 THEN 1
            WHEN monetary <= m40 AND monetary >= m20 THEN 2
            WHEN monetary <= m60 AND monetary >= m40 THEN 3
            WHEN monetary <= m80 AND monetary >= m60 THEN 4
            WHEN monetary <= m100 AND monetary >= m80 THEN 5
        END AS m_score,
        CASE 
            WHEN frequency <= f20 THEN 1
            WHEN frequency <= f40 AND frequency >= f20 THEN 2
            WHEN frequency <= f60 AND frequency >= f40 THEN 3
            WHEN frequency <= f80 AND frequency >= f60 THEN 4
            WHEN frequency <= f100 AND frequency >= f80 THEN 5
        END AS f_score,
        CASE 
            WHEN recency <= d20 THEN 5
            WHEN recency <= d40 AND recency >= d20 THEN 4
            WHEN recency <= d60 AND recency >= d40 THEN 3
            WHEN recency <= d80 AND recency >= d60 THEN 2
            WHEN recency <= d100 AND recency >= d80 THEN 1
        END AS r_score                        
    FROM `Sales.quantiles`
);
