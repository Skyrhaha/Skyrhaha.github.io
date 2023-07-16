#!/usr/bin/python3
# coding:utf8

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
            getPageDataAndSaveFile(data)
        else:
            queueLock.release()
        time.sleep(1)

def getPageDataAndSaveFile(page):
    print(f'get page {page}...')
    pass

queueLock = threading.Lock()
workQueue = queue.Queue(0)
threads = []

# 创建新线程
for i in range(20):
    thread = myThread(threadID=i+1, name=f'Thread-{i+1}', q=workQueue)
    thread.start()
    threads.append(thread)

# 填充队列
queueLock.acquire()
for page in range(1000):
    workQueue.put(page+1)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")