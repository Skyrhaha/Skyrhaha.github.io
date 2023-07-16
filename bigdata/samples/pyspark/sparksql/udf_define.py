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

    # 方式一: 使用sparksession.udf.register使用，支持SQL+DSL
    # 构建一个rdd
    rdd = sc.parallelize([1,2,3,4,5,6,7]).map(lambda x:[x])
    # 构建DataFrame
    df = rdd.toDF(['num'])

    # UDF处理函数定义num_ride_10
    def num_ride_10(num):
        return num*10

    # 注册UDF
    # 参数1: 名称，仅可以用于SQL分格
    # 参数2: 处理逻辑
    # 参数3: 返回值类型，必须与指定
    # 返回值对象: UDF对象，仅用于DSL风格
    udf2 = spark.udf.register("udf1", num_ride_10, IntegerType())
    
    # SQL风格使用
    df.selectExpr("udf1(num)").show()

    # DSL风格使用
    # udf2作为方法使用，传入的参数一定是Column对象
    df.select(udf2(df['num'])).show()

    # 方式二: 通果pyspark.sql.functions.udf使用,仅支持DSL
    print('-----------use pyspark.sql.function.udf使用---------------------')
    udf3 = F.udf(num_ride_10, IntegerType())
    df.select(udf3(df['num'])).show()