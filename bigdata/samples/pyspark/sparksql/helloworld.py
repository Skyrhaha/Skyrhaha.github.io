# coding:utf8

from pyspark import SparkConf,SparkContext

# # 环境变量使用
# import os
# os.environ['TEST']='env test'
# print(os.getenv('TEST')) # => env test

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[*]").setAppName("WorldCountApp")

    #通过SparkConf对象构建SparkContext
    sc = SparkContext(conf=conf)

    # 读取文件
    # file_rdd = sc.textFile("hdfs://node1:8020/input/words.txt")
    file_rdd = sc.textFile("./data/input/words.txt")

    words_rdd = file_rdd.flatMap(lambda line:line.split(" "))

    words_with_one_rdd = words_rdd.map(lambda x : (x, 1))

    result_rdd = words_with_one_rdd.reduceByKey(lambda a,b : a+b)

    result = result_rdd.collect()
    
    print(result)
    for line in result:
        print(line)
    

    # 保存
    result_rdd.saveAsTextFile('./data/output/words-result/')

    sc.stop()