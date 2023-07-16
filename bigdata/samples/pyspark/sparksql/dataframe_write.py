# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,IntegerType,StringType
import time

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]") \
        .config("spark.sql.shuffle.partitions", 2) \
        .getOrCreate()

    sc = spark.sparkContext

    schema = StructType().add("user_id", StringType(), nullable=True) \
        .add("movie_id", IntegerType(), nullable=True) \
        .add("rank", IntegerType(), nullable=True) \
        .add("ts", StringType(), nullable=True) \

    df = spark.read.format("csv") \
        .option("sep", "\t") \
        .option("header", False) \
        .option("encoding", "utf-8") \
        .schema(schema=schema) \
        .load("data/input/u.data")
    
    # Write text写出,只能写出一个列，需要将df转换为单列df
    df.select(F.concat_ws("---", "user_id", "movie_id", "rank", "ts")) \
        .write \
        .mode("overwrite") \
        .format("text") \
        .save("data/output/text/")

    # Write csv
    df.write \
        .mode("overwrite") \
        .format("csv") \
        .option("sep", ";") \
        .option("header", True) \
        .save("data/output/csv/")

    # Write json
    df.write \
        .mode("overwrite") \
        .format("json") \
        .save("data/output/json/")

    # Write parquet
    df.write \
        .mode("overwrite") \
        .format("parquet") \
        .save("data/output/parquet/")