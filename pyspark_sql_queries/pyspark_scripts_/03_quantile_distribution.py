# Calculate approximate percentiles for quantiles (0 to 100)
rfm_quantile = spark.sql("""
    SELECT
        a.*,
        -- Monetary Quantiles
        b.percentile[1] AS m20, b.percentile[2] AS m40, b.percentile[3] AS m60, b.percentile[4] AS m80, b.percentile[5] AS m100,
        -- Frequency Quantiles
        c.percentile[1] AS f20, c.percentile[2] AS f40, c.percentile[3] AS f60, c.percentile[4] AS f80, c.percentile[5] AS f100,
        -- Recency Quantiles
        d.percentile[1] AS d20, d.percentile[2] AS d40, d.percentile[3] AS d60, d.percentile[4] AS d80, d.percentile[5] AS d100
    FROM rfm a
    CROSS JOIN (SELECT APPROX_PERCENTILE(monetary, ARRAY(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)) AS percentile FROM rfm) b
    CROSS JOIN (SELECT APPROX_PERCENTILE(frequency, ARRAY(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)) AS percentile FROM rfm) c
    CROSS JOIN (SELECT APPROX_PERCENTILE(recency, ARRAY(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)) AS percentile FROM rfm) d
""")

rfm_quantile.createOrReplaceTempView("rfm_quantile")
rfm_quantile.show()
