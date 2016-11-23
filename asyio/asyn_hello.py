#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: asy_hello.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-23 23:07:36

#=====================================
import threading
import asyncio

async def hello():
    print("Hello world!(%s)" % threading.currentThread())
    await asyncio.sleep(1)
    print("Hello again!(%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
