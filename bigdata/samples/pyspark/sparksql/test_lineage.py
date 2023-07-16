# coding:utf8

from re import S
from pyspark.sql import SparkSession,DataFrame
from pyspark.sql.types import StructType, StringType, IntegerType
import os

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]").getOrCreate()

    df = spark.read.format('json').load(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.json")
    df.printSchema()
    df.show()

    # 参数1: 展示多少条数据，默认20
    # 参数2: 是否对列进行解读，如果超过20，后续以...替代
    df.show(20, False)  # 表数据
    df.createOrReplaceTempView("ods_people") # 创建t_people表

    # SQL风格
    df2 = spark.sql("""
    SELECT * FROM ods_people WHERE age < 200
    """)

    df2.write.saveAsTable("ods_people2")

