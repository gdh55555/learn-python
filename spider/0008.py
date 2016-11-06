#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0008.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-06 16:26:40

#=====================================
"""
一个HTML文件，找出里面的正文
"""
from HTMLParser import HTMLParser
from re import sub
import urllib2
import sys

class MyHTMLParser1(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.text.append("\n");

    def handle_data(self, data) :
        if len(data.strip()) > 0:
            self.text.append(data.strip())

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = []

    def handle_starttag(self, tag, attrs):
        #TagStack.append(tag)
        if tag == "body" or tag == "p":
            TagStack.append(tag)

    def handle_endtag(self, tag, tag_flag = True):
        #while tag_flag == True:
        #    if tag == TagStack[-1]:
        #        TagStack.pop()
        #        tag_flag = False
        #    else:
        #        TagStack.pop()
        if tag == "body" or tag == "p":
            TagStack.pop()

    def handle_data(self, data):
        if data.strip() and "body" in TagStack and "p" in TagStack:
            self.text.append("\n" + data.strip())

def GetText():
    url = "http://www.baidu.com"
    html = urllib2.urlopen(url).read()
#    html_code = sub('<script[^>]*?>[^>]*?</script>', '', html)
#    html_code = sub('<script>.*?</script>', '', html_code)

    parse = MyHTMLParser()
    parse.feed(html)
    parse.close()

    return ''.join(parse.text).strip()

if __name__ == "__main__":
    TagStack = []
    reload(sys)
    sys.setdefaultencoding("utf-8")
    print GetText()
