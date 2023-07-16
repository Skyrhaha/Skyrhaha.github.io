# coding:utf8

from pyspark import SparkConf,SparkContext

# # 环境变量使用
# import os
# os.environ['TEST']='env test'
# print(os.getenv('TEST')) # => env test

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[*]").setAppName("rdd")

    #通过SparkConf对象构建SparkContext
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([0,2,3,4,6], 3) \
        .map(lambda x: x+3) \
        .glom()
    print(rdd.getNumPartitions())
    print(rdd.collect())

    file_rdd = sc.textFile("./data/input/words.txt", minPartitions=5)
    print(file_rdd.getNumPartitions())
    print(file_rdd.collect())
    sc.stop()