# coding:utf8

from re import S
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]").getOrCreate();

    sc = spark.sparkContext

    # 基于RDD转换构建DataFrame
    print('---------------------Base RDD-----------------------')

    rdd = sc.textFile("data/input/people.txt") \
        .map(lambda x: x.split(",")) \
        .map(lambda x: (x[0], int(x[1])))

    df = spark.createDataFrame(rdd, schema=['name', 'age'])
    df.printSchema()  # 表结构

    # 参数1: 展示多少条数据，默认20
    # 参数2: 是否对列进行解读，如果超过20，后续以...替代
    df.show(20, False)  # 表数据
    df.createTempView("t_people") # 创建t_people表

    # SQL风格
    spark.sql("""
    SELECT * FROM t_people WHERE age < 200
    """).show()

    # 基于StructType构建DataFrame
    print('---------------------Base StructType-----------------------')
    schema = StructType().add("name", StringType(), nullable=True) \
        .add("age", IntegerType(), nullable=False)
    df2 = spark.createDataFrame(rdd, schema=schema)
    df2.printSchema()
    df2.show()

    print('---------------------Base toDF-----------------------')
    df3 = rdd.toDF(["name", "age"])
    df3.printSchema()
    df3.show()
    df4 = rdd.toDF(schema=schema)
    df4.printSchema()
    df4.show()