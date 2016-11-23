#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: async_wget.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-23 23:11:03

#=====================================
import asyncio

@asyncio.coroutine
def wget(host):
    print("wget %s ..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    print("get from %s...." % host)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' %host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    print("write from %s...." % host)
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print("%s header > %s" %(host, line.decode("utf-8").rstrip()))

    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

