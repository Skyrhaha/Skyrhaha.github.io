# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,IntegerType,StringType
import os

dburl = os.getenv('DB_URL')
dbuser = os.getenv('DB_USER')
dbpassword = os.getenv('DB_PWD')
print(dburl, dbuser,dbpassword)

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
        .load("data/input/u.data.small")
    
    # Write jdbc
    # write会自动创建数据库表
    df.write \
        .mode("overwrite") \
        .format("jdbc") \
        .option("url", dburl)  \
        .option("dbtable", "movie_data") \
        .option("user", dbuser) \
        .option("password", dbpassword) \
        .save()

    # Read jdbc
    rdf = spark.read.format("jdbc").option("url", dburl) \
        .option("user", dbuser) \
        .option("password", dbpassword) \
        .option("dbtable", "movie_data") \
        .load()
    rdf.show()

