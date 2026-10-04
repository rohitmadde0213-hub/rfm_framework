from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import DecimalType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("RFM_Step1_Invoice_Aggregation") \
    .getOrCreate()

# Load raw sales data
df = spark.read.option('header', 'true').csv('sales.csv')
df.createOrReplaceTempView("sales")

# Aggregate total sales and item counts per invoice
bills = spark.sql("""
    WITH bills AS (
        SELECT 
            InvoiceNo,
            (CAST(Quantity AS DECIMAL(10, 2)) * CAST(UnitPrice AS DECIMAL(10, 2))) AS AMOUNT
        FROM sales
    )
    SELECT
        InvoiceNo, 
        ROUND(SUM(AMOUNT), 2) AS total, 
        COUNT(*) AS counts
    FROM bills
    GROUP BY InvoiceNo
""")

bills.createOrReplaceTempView("bills")
bills.show()
