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

    rdd = sc.textFile("./data/input/order.text")
    rdd = rdd.flatMap(lambda x: x.split('|'))
    rdd = rdd.map(lambda x : json.loads(x))
    rdd = rdd.filter(lambda x : x['areaName'] == '北京')
    rdd = rdd.map(lambda x: x['areaName'] + '_' + x['category'])
    rdd = rdd.distinct()

    print(rdd.collect())
    sc.stop()