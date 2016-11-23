#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: demo2.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-22 22:17:10

#=====================================

import time, threading

def loop():
    print("thread %s is running..." %threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >> %s" %(threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s is ended." %threading.current_thread().name)

print("thread %s is running..." %threading.current_thread().name)
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print("thread %s is ended." %threading.current_thread().name)

