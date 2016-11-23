#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: task_master.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-22 22:45:07

#=====================================
import time, sys, queue
from multiprocessing.managers import BaseManager


#从Basemanager继承的Queuemanger
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上，callable参数继承queue对象
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#connect server
#server_addr = '114.214.176.32'
server_addr = '127.0.0.1'
print("Connect to server %s..." %server_addr)
manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')
#start queue
manager.connect()
#get queue from net
task = manager.get_task_queue()
result = manager.get_result_queue()
#put some task in it
for i in range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d * %d..." %(n,n))
        r = '%d * %d = %d' %(n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print("task queue is empty")

#exit
print("worker exit.")
