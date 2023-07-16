# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,IntegerType,StringType
import os
import string

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

    # 方式一: 使用sparksession.udf.register使用，支持SQL+DSL
    # 构建一个rdd
    rdd = sc.parallelize([[1],[2],[3]])
    # 构建DataFrame
    df = rdd.toDF(['num'])

    # UDF处理函数定义num_ride_10
    def split_line(num):
        return {"num":num, "letter_str":string.ascii_letters[num]}

    struct_type = StructType().add("num", IntegerType(), nullable=True) \
        .add("letter_str", StringType(), nullable=True)

    udf2 = spark.udf.register("udf1", split_line, struct_type)
    
    df.select(udf2(df['num'])).show(truncate=False)
    df.selectExpr("udf1(num)").show(truncate=False)

    # 方式二: 通果pyspark.sql.functions.udf使用,仅支持DSL
    print('-----------use pyspark.sql.function.udf使用---------------------')
    udf3 = F.udf(split_line, struct_type)
    df.select(udf3(df['num'])).show(truncate=False)