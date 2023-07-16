# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StringType

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]").getOrCreate();

    sc = spark.sparkContext

    print('----------------TEXT-----------------------')
    schema = StructType().add("data", StringType(), nullable=True)
    df = spark.read.format("text") \
        .schema(schema=schema) \
        .load("data/input/people.txt")
    df.printSchema()
    df.show()

    print('----------------JSON-----------------------')
    df = spark.read.format("json").load("data/input/people.json")
    df.printSchema()
    df.show()

    print('----------------CSV-----------------------')
    df = spark.read.format("csv") \
        .option("sep", ";") \
        .option("header", True) \
        .option("encoding", "utf-8") \
        .schema("name STRING, age INT, job STRING") \
        .load("data/input/people.csv")
    df.printSchema()
    df.show()
   
    print('------------------PARQUET---------------------')
    df = spark.read.format("parquet").load("data/input/users.parquet")
    df.printSchema()
    df.show()
   