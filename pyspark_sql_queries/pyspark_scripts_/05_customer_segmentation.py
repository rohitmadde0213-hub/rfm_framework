# Map RFM scores to strategic customer marketing segments
rfm_segmented = spark.sql("""
    SELECT
        CustomerID,
        recency, frequency, monetary,
        r_score, f_score, m_score,
        fm_score,
        CASE
            WHEN (r_score = 5 AND fm_score = 5) OR (r_score = 5 AND fm_score = 4) OR (r_score = 4 AND fm_score = 5) THEN 'Champions'
            WHEN (r_score = 5 AND fm_score = 3) OR (r_score = 4 AND fm_score = 4) OR (r_score = 3 AND fm_score = 5) OR (r_score = 3 AND fm_score = 4) THEN 'Loyal Customers'
            WHEN (r_score = 5 AND fm_score = 2) OR (r_score = 4 AND fm_score = 2) OR (r_score = 3 AND fm_score = 3) OR (r_score = 4 AND fm_score = 3) THEN 'Potential Loyalists'
            WHEN r_score = 5 AND fm_score = 1 THEN 'Recent Customers'
            WHEN (r_score = 4 AND fm_score = 1) OR (r_score = 3 AND fm_score = 1) THEN 'Promising'
            WHEN (r_score = 3 AND fm_score = 2) OR (r_score = 2 AND fm_score = 3) OR (r_score = 2 AND fm_score = 2) THEN 'Customers Needing Attention'
            WHEN r_score = 2 AND fm_score = 1 THEN 'About to Sleep'
            WHEN (r_score = 2 AND fm_score = 5) OR (r_score = 2 AND fm_score = 4) OR (r_score = 1 AND fm_score = 3) THEN 'At Risk'
            WHEN (r_score = 1 AND fm_score = 5) OR (r_score = 1 AND fm_score = 4) THEN 'Cant Lose Them'
            WHEN r_score = 1 AND fm_score = 2 THEN 'Hibernating'
            WHEN r_score = 1 AND fm_score = 1 THEN 'Lost'
        END AS rfm_segment
    FROM rfm_final
""")

rfm_segmented.createOrReplaceTempView("rfm_segments")
rfm_segmented.show()
