# coding:utf8

from pyspark import SparkConf,SparkContext
import json

# # 环境变量使用
# import os
# os.environ['TEST']='env test'
# print(os.getenv('TEST')) # => env test

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[*]").setAppName("rdd")

    #通过SparkConf对象构建SparkContext
    sc = SparkContext(conf=conf)

    sc.setCheckpointDir("./data/checkpoint/")

    rdd1 = sc.textFile("./data/input/words.txt")
    rdd2 = rdd1.flatMap(lambda x: x.split(' '))
    rdd3 = rdd2.map(lambda x : (x, 1))
    rdd3.checkpoint()
    
    rdd3.reduceByKey(lambda a,b: a+b)
    print(rdd3.collect())


    sc.stop()