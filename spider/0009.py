#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0009.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-06 20:45:23

#=====================================

#一个HTML文件，找出里面的链接。

from HTMLParser import HTMLParser
import sys
import urllib2

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for(variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)

def GetLinks(url):
    html = urllib2.urlopen(url).read()
    parser = MyHTMLParser()
    parser.feed(html)
    print parser.links

if __name__ == "__main__":
    url = ""
    if len(sys.argv) == 1:
        url = "http://www.baidu.com"
    else:
        url = sys.argv[1]
    #sys.setdefaultencoding("utf-8")
    GetLinks(url)
