#!/usr/bin/python  
#-*- coding:utf-8 -*-  
__author__ = "goodhe"

#=====================================

#File Name: 0006.py
#Mail: gdhe55555@gmail.com  
#Created Time: 2016-11-03 16:11:32

#=====================================
# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import glob
import os
import re
from collections import Counter

def dir_list(dir_name = "text"):
    #return glob.glob("*.txt")
    return os.listdir(dir_name)

def wc(file_name):
    datalist = []
    with open(file_name, 'r') as f:
        for line in f:
            content = re.sub("\"\.|,", "",  line)
            datalist.extend(content.strip().split(' '))
    return Counter(datalist).most_common(1)

def most_comm(dir_name):
    for i in dir_list():
        print wc(os.path.join(dir_name, i))

if __name__ == "__main__":
    most_comm("text")
    #print map(wc, dir_list())

