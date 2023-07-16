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
   
    # 注册临时表
    df.createTempView("t_score") #注册临时视图(表)
    df.createOrReplaceTempView("t_score2") # 注册或替换
    # 注册全局表,可跨SparkSession使用
    # 使用时前面添加global_temp.
    df.createGlobalTempView("t_global_score")

    spark.sql("SELECT subject,COUNT(*) AS cnt FROM t_score GROUP BY subject").show()
    spark.sql("SELECT subject,COUNT(*) AS cnt FROM t_score2 GROUP BY subject").show()
    spark.sql("SELECT subject,COUNT(*) AS cnt FROM global_temp.t_global_score GROUP BY subject").show()