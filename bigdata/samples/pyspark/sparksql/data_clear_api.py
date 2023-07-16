# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,IntegerType,StringType
import time

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]") \
        .config("spark.sql.shuffle.partitions", 2) \
        .getOrCreate()

    sc = spark.sparkContext

    schema = StructType().add("user_id", StringType(), nullable=True) \
        .add("movie_id", IntegerType(), nullable=True) \
        .add("rank", IntegerType(), nullable=True) \
        .add("ts", StringType(), nullable=True) \

    df = spark.read.format("csv") \
        .option("sep", ";") \
        .option("header", True) \
        .load("data/input/people.csv")

    # 数据清洗: 数据去重
    # dropDuplicates()无参使用,整体去重
    df.dropDuplicates().show()

    # 根据age,job去重
    print("根据age,job去重...")
    df.dropDuplicates(['age', 'job']).show()

    # 数据清洗：缺失值处理
    # 无参使用：只要列中有空就删除这一行数据
    print("缺失值dropna处理...")
    df.dropna().show()
    # thresh=3,最少满足3个有效列，不满足就删除行
    df.dropna(thresh=3).show()
    # 在name,age列必须达到2个
    df.dropna(thresh=2,subset=['name', 'age']).show()

    # 缺失值填充fillna
    df.fillna("loss").show()
    # 指定列填充
    df.fillna("N/A", subset=['job']).show()

    #设定一个字典，对所有列进行填充
    df.fillna({"name":"未知姓名", "age":1, "job": "worker"}).show()