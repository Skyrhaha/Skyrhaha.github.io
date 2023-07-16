# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]").getOrCreate();

    sc = spark.sparkContext

    # 1. 使用SQL风格
    print("------------------Use SQL-------------------------------------------")
    rdd = sc.textFile("data/input/words.txt") \
        .flatMap(lambda x: x.split(" ")) \
        .map(lambda x:[x])
    df = rdd.toDF(["word"])
    df.createTempView("t_word")
    spark.sql("SELECT word,count(*) AS cnt FROM t_word GROUP BY word ORDER BY cnt DESC").show()

    # 2. 使用DSL风格
    print("------------------Use DSL-------------------------------------------")
    df = spark.read.format("text").load("data/input/words.txt")
    df2 = df.withColumn("value", F.explode(F.split(df['value'], " ")))
    df2.groupBy("value") \
        .count() \
        .withColumnRenamed("value", "word") \
        .withColumnRenamed("count", "cnt") \
        .orderBy("cnt", ascending=False) \
        .show()
