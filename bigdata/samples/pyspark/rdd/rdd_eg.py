# coding:utf8

from pyspark import SparkConf,SparkContext, StorageLevel
import json
import jieba
from operator import add

# # 环境变量使用
# import os
# os.environ['TEST']='env test'
# print(os.getenv('TEST')) # => env test

def append_words(data):
    if data == '传智播':
        data = '传智播客'
    return data

def extract_user_and_word(data):
    user_id = data[0]
    user_content = data[1]

    rl = list()
    for w in jieba.cut_for_search(user_content):
        if w not in ['谷']:
            rl.append((user_id+'_'+w, 1))
    
    return rl

if __name__ == '__main__':
    # content = '小明硕士毕业于中国科学院，后在清华大学深造'
    # result = jieba.cut(content, True)
    # print(list(result))
    # print(type(result))

    # result = jieba.cut(content, False)
    # print(list(result))

    # result = jieba.cut_for_search(content)
    # print(list(result))

    conf = SparkConf().setMaster("local[*]").setAppName("rdd")

    #通过SparkConf对象构建SparkContext
    sc = SparkContext(conf=conf)
    rdd = sc.textFile("./data/input/SogouQ.txt")
    rdd = rdd.map(lambda x: x.split('\t'))

    rdd.persist(StorageLevel.DISK_ONLY)

    # 用户搜索关键词分析
    # print(rdd.takeSample(True, 3))
    content_rdd = rdd.map(lambda x: x[2])
    kw_rdd = content_rdd.flatMap(lambda x: jieba.cut_for_search(x))
    ft_rdd = kw_rdd.filter(lambda x: x not in ['谷', '帮', '客'])
    final_rdd = ft_rdd.map(append_words).map(lambda x: (x, 1))
    result1 = final_rdd.reduceByKey(lambda a,b: a+b) \
        .sortBy(lambda x: x[1], ascending=False, numPartitions=1) \
        .take(5)
    print(result1)
    
    # 用户和关键词组合
    user_content_rdd = rdd.map(lambda x: (x[1], x[2]))
    ucrdd = user_content_rdd.flatMap(extract_user_and_word)
    result2 = ucrdd.reduceByKey(lambda a,b: a+b) \
        .sortBy(lambda x:x[1], ascending=False, numPartitions=1) \
        .take(5)
    print(result2)


    # 热门时间分析
    time_rdd = rdd.map(lambda x: x[0])
    hour_rdd = time_rdd.map(lambda x: (x.split(':')[0],1))
    result3 = hour_rdd.reduceByKey(add) \
        .sortBy(lambda x:x[1], ascending=False, numPartitions=1) \
        .take(5)
    print(result3)
    sc.stop()