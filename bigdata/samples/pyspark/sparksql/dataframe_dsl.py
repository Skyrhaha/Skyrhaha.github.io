# coding:utf8

from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]").getOrCreate();

    sc = spark.sparkContext

    df = spark.read.format("csv") \
        .schema("id STRING,subject STRING, score INT") \
        .load("data/input/stu_score.txt") 
    df.printSchema()
    df.show()
   
    # Colunm对象获取
    id_column = df['id']
    subject_column = df['subject']

    # DSL风格演示:以下输出一样
    print('-------------------select()---------------------')
    df.select(["id", "subject"]).show()
    df.select("id", "subject").show()
    df.select(id_column, subject_column).show()

    # filter
    print('-------------------filter()---------------------')
    df.filter("score < 99").show()
    df.filter(df["score"]<99).show()

    # where
    print('-------------------where()---------------------')
    df.where("score < 99").show()
    df.where(df["score"]<99).show()

    # group by
    print('-------------------groupBy()---------------------')
    df.groupBy("subject").count().show()
    df.groupBy(df["subject"]).count().show()

    # groupBy返回值不是DataFrame,是GroupedData
    # GroupedData类似SQL分组后的数据结构
    # 后面接上聚合: count,sum,avg,min,max...
    r = df.groupBy("subject")
    print(r)