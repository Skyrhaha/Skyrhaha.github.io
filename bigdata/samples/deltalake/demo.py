# 启动
# pyspark --packages io.delta:delta-core_2.12:2.1.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"

# pip install delta-spark
# pip install pyspark==3.2.1
# pip install delta-spark==2.0
from delta import *
from pyspark.sql import SparkSession

builder = SparkSession.builder.master("local[*]").appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# data = spark.range(0, 5)
# data.write.format("delta").save("/tmp/delta-table")

df=spark.read.format('delta').load('/tmp/delta-table')
df.printSchema()
df.show()

