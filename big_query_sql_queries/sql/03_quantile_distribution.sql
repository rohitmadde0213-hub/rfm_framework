-- Step 4: Calculate 100th percentile quantiles for RFM scoring
CREATE OR REPLACE TABLE `Sales.quantiles` AS
SELECT 
    a.*,
    -- Monetary Quantiles
    b.percentile[OFFSET(20)] AS m20,
    b.percentile[OFFSET(40)] AS m40,
    b.percentile[OFFSET(60)] AS m60,
    b.percentile[OFFSET(80)] AS m80,
    b.percentile[OFFSET(100)] AS m100,
    -- Frequency Quantiles
    c.percentile[OFFSET(20)] AS f20,
    c.percentile[OFFSET(40)] AS f40,
    c.percentile[OFFSET(60)] AS f60,
    c.percentile[OFFSET(80)] AS f80,
    c.percentile[OFFSET(100)] AS f100,
    -- Recency Quantiles
    d.percentile[OFFSET(20)] AS d20,
    d.percentile[OFFSET(40)] AS d40,
    d.percentile[OFFSET(60)] AS d60,
    d.percentile[OFFSET(80)] AS d80,
    d.percentile[OFFSET(100)] AS d100
FROM `Sales.rfm` a
CROSS JOIN (SELECT APPROX_QUANTILES(monetary, 100) AS percentile FROM `Sales.rfm`) b
CROSS JOIN (SELECT APPROX_QUANTILES(frequency, 100) AS percentile FROM `Sales.rfm`) c
CROSS JOIN (SELECT APPROX_QUANTILES(recency, 100) AS percentile FROM `Sales.rfm`) d;
