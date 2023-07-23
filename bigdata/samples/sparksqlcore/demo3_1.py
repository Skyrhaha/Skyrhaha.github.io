from pyspark.sql import SparkSession
import os

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

df = spark.read.json('data/student.json')
df.show()

df.createOrReplaceTempView('student')

spark.sql('select name from student where age > 18').show()