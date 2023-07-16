# coding:utf8

from array import ArrayType
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import ArrayType,IntegerType,StringType
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

    # 方式一: 使用sparksession.udf.register使用，支持SQL+DSL
    # 构建一个rdd
    rdd = sc.parallelize([['hadoop flink spark'], ['hadoop spark java']])
    # 构建DataFrame
    df = rdd.toDF(['line'])

    # UDF处理函数定义num_ride_10
    def split_line(data):
        return data.split(" ") #return array

    # 注册UDF
    # 参数1: 名称，仅可以用于SQL分格
    # 参数2: 处理逻辑
    # 参数3: 返回值类型，必须与指定
    # 返回值对象: UDF对象，仅用于DSL风格
    udf2 = spark.udf.register("udf1", split_line, ArrayType(StringType()))
    
    df.createTempView('t_lines')
    # SQL风格使用
    spark.sql("SELECT UDF1(line) FROM t_lines").show(truncate=False)

    # DSL风格使用
    # udf2作为方法使用，传入的参数一定是Column对象
    df.select(udf2(df['line'])).show(truncate=False)

    # 方式二: 通果pyspark.sql.functions.udf使用,仅支持DSL
    print('-----------use pyspark.sql.function.udf使用---------------------')
    udf3 = F.udf(split_line, ArrayType(StringType()))
    df.select(udf3(df['line'])).show(truncate=False)