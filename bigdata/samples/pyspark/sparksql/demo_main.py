# coding:utf8

"""
1. 各省 销售 指标 每个省份的销售额统计
2. TOP3 销售省份中, 有多少家店铺 日均销售额 1000+
3. TOP3 省份中 各个省份的平均单单价
4. TOP3 省份中, 各个省份的支付类型比例

storeDistrict 店铺所在行政区
storeProvince 店铺所在省份
storeID 店铺ID
storeName 店铺名称
dateTS 订单日期
orderID 订单ID
receivable 收款金额
payType 付款类型
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.storagelevel import StorageLevel
from pyspark.sql.types import StringType
import os

dburl = os.getenv('DB_URL')
dbuser = os.getenv('DB_USER')
dbpassword = os.getenv('DB_PWD')
print(dburl, dbuser,dbpassword)

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("SparkSQL Example") \
        .master("local[*]") \
        .getOrCreate()
        # .config("spark.sql.shuffle.partitions", "2") \
        # .config("spark.sql.warehouse.dir", "hdfs://node1:8020/user/hive/warehouse") \
        # .config("hive.metastore.uris", "thrift://node3:9083") \
        # .enableHiveSupport() \
        # .getOrCreate()

    df = spark.read.format('json').load("data/input/minimini.json") \
        .dropna(thresh=1, subset=['storeProvince']) \
        .filter("storeProvince != 'null'") \
        .filter("receivable < 10000") \
        .select("storeProvince", "storeID", "receivable", "dateTS", "payType")

    # 各省销售额统计
    province_sale_df = df.groupBy("storeProvince").sum("receivable") \
        .withColumnRenamed("sum(receivable)", "money") \
        .withColumn("money", F.round("money", 2)) \
        .orderBy("money",ascending=False)
    province_sale_df.show(truncate=False)

    province_sale_df.write.mode('overwrite').format('jdbc')\
        .option("url", dburl)  \
        .option("dbtable", "province_sale") \
        .option("user", dbuser) \
        .option("password", dbpassword) \
        .save()

    # 写到Hive
    # province_sale_df.write.mode('overwrite').saveAsTable("default.province_sale", "parquet")

    # TOP3 销售省份中, 有多少家店铺 日均销售额 1000+
    top3_province_df = province_sale_df.limit(3).select("storeProvince").withColumnRenamed("storeProvince", "top3_province")
    top3_province_df_joined = df.join(top3_province_df, on=df['storeProvince'] == top3_province_df['top3_province'])
    top3_province_df_joined.show()

    # 缓存
    top3_province_df_joined.persist(StorageLevel.MEMORY_AND_DISK)

    province_hot_store_count_df = top3_province_df_joined.groupBy("storeProvince", "storeID",
                                    F.from_unixtime(df['dateTS'].substr(0,10), 'yyyy-MM-dd').alias('day')) \
        .sum("receivable").withColumnRenamed("sum(receivable)", "money") \
        .filter("money > 1000") \
        .dropDuplicates(subset=['storeID']) \
        .groupBy("storeProvince").count()
    province_hot_store_count_df.show()

    
    province_hot_store_count_df.write.mode('overwrite').format('jdbc')\
        .option("url", dburl)  \
        .option("dbtable", "province_hot_store_count") \
        .option("user", dbuser) \
        .option("password", dbpassword) \
        .save()

    # TOP3 省份中 各个省份的平均单单价
    top3_province_order_avg_df = top3_province_df_joined.groupBy("storeProvince").avg("receivable") \
        .withColumnRenamed("avg(receivable)", "avg_money") \
        .withColumn("avg_money", F.round('avg_money', 2)) \
        .orderBy('avg_money', ascending=False) 
    top3_province_order_avg_df.show()

    top3_province_order_avg_df.write.mode('overwrite').format('jdbc')\
        .option("url", dburl)  \
        .option("dbtable", "top3_province_order_avg") \
        .option("user", dbuser) \
        .option("password", dbpassword) \
        .save()

    # TOP3 省份中, 各个省份的支付类型比例

    def udf_func(percent):
        return str(round(percent * 100, 2))+'%'

    myudf = F.udf(udf_func, StringType())

    top3_province_df_joined.createTempView("province_pay")
    pay_type_df = spark.sql("""
        SELECT storeProvince,payType,(COUNT(payType)/total) AS percent FROM
        (SELECT storeProvince,payType, count(1) OVER(PARTITION BY storeProvince) AS total FROM province_pay) AS sub
        GROUP BY storeProvince,payType,total
        ORDER BY storeProvince,percent DESC
    """).withColumn("percent", myudf("percent"))
    pay_type_df.show()

    pay_type_df.write.mode('overwrite').format('jdbc')\
        .option("url", dburl)  \
        .option("dbtable", "top3_pay_type") \
        .option("user", dbuser) \
        .option("password", dbpassword) \
        .save()

    top3_province_df_joined.unpersist()
