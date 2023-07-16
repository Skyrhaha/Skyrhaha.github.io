# coding:utf8

from pyspark.sql import SparkSession
import pandas as pd

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]").getOrCreate();

    sc = spark.sparkContext

    pdf = pd.DataFrame(
        {
            "id" : [1,2,3],
            "name": ["张三", "李四", "王五"],
            "age": [11,21,31]
        }
    )

    df = spark.createDataFrame(pdf)
    df.printSchema()
    df.show()
   