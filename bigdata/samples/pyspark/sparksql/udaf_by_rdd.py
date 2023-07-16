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

    rdd = sc.parallelize([1,2,3,4,5], 3)
    df = rdd.map(lambda x:[x]).toDF(['num'])

    #折中的方式 这是使用RDD的mapPartitions算子来完成聚合操作
    #如果用mapPartitions API完成UDAF聚合,一定要单分区
    single_partition_rdd = df.rdd.repartition(1)

    def process(iter):
        sum = 0
        for row in iter:
            sum += row['num']
        return [sum]  #一定要嵌套list,因为mapPartitions方法要求

    print(single_partition_rdd.mapPartitions(process).collect())