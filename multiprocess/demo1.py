#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: demo1.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-21 23:27:49

#=====================================

from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process %s (%s)..." %(name, os.getpid()))

if __name__ == "__main__":
    print("Parent process %s." %os.getpid())
    p = Process(target=run_proc, args=("test",))
    print("Child process will start")
    p.start();
    p.join();
    print("Child process end")


