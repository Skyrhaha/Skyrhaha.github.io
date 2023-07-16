# coding:utf8

from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("test").master("local[*]").getOrCreate();

    sc = spark.sparkContext

    df = spark.read.csv("data/input/stu_score.txt", sep=",", header=False)
    df2 = df.toDF("id", "name", "score")
    df2.printSchema()  # 表结构
    df2.show()  # 表数据
    df2.createTempView("t_score") # 创建t_score表

    # SQL风格
    spark.sql("""
    SELECT * FROM t_score WHERE name='语文' LIMIT 5
    """).show()

    # DSL风格
    df2.where("name='语文'").limit(5).show()