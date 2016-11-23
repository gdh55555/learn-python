#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: task_master.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-22 22:45:07

#=====================================
import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务到队列
task_queue = queue.Queue()
#接收结果到队列
result_queue = queue.Queue()

#从Basemanager继承的Queuemanger
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上，callable参数继承queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
#绑定端口5000，设置验证码‘abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
#start queue
manager.start()
#get queue from net
task = manager.get_task_queue()
result = manager.get_result_queue()
#put some task in it
for i in range(10):
    n = random.randint(0, 100000)
    print("Put task %d..." %n)
    task.put(n)

print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Result:%s " %r)

#shutdown
manager.shutdown()
print("master exit.")
