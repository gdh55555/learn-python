#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0011.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-07 09:10:31

#=====================================

#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

import os

def Words(path):
    filterwords = []
    f = open(path)
    for word in f.readlines():
        filterwords.append(word.strip('\n'))

    return filterwords

if __name__ == "__main__":
    filteredwords = Words("filtered_words.txt")
    while(True):
        input = raw_input("input your line>>>").split()
        if set(input).intersection(filteredwords):
            print "Freedom"
        else:
            print "Human Rights"
