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

    rdd = sc.textFile("./data/input/words.txt")
    rdd = rdd.flatMap(lambda x: x.split(' '))
    rdd = rdd.map(lambda x: (x, 1))
    result = rdd.countByKey()

    print(rdd.collect())
    print(result.items())


    rdd = sc.parallelize(range(1,3))
    result = rdd.reduce(lambda a,b: a+b)
    print(result)

    rdd = sc.parallelize([19, 0, 9])
    result = rdd.first()
    print(result)
    print(rdd.take(2))
    print(rdd.top(2))
    print(rdd.count())

    print(sc.parallelize(range(1,100)).takeSample(False, 10))
    print(sc.parallelize(range(10,30)).takeOrdered(3, lambda x: -x))

    sc.parallelize([1, 4,5,9]).foreach(lambda x : print(x * 100))

    # sc.parallelize(range(1,100)).saveAsTextFile("./data/output/action_save01")

    rdd = sc.parallelize([1,2,3,4,5,6,7], 3).mapPartitions(lambda x:x)
    print(rdd.collect())
    sc.stop()