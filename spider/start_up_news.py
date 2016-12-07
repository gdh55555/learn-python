#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: start_up_news.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-29 23:14:38

#=====================================

import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = "http://news.dbanotes.net"

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    visited |= {url}

    print('has visited: ' + str(cnt) + '  now visiting <----' + url)
    cnt += 1
    urlop = urllib.request.urlopen(url)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('add to queue-----> ' + x)
