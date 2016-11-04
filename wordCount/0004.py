#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = "goodhe"

#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import re
from collections import Counter

def create_list(file_name):
    datalist = []
    with open(file_name, 'r') as f:
        for line in f:
            content = re.sub("\"|,|\.", "", line)
            datalist.extend(content.strip().split(' '))
    return datalist

def match_list(file_name):
    with open(file_name, 'r') as f:
        word_pat = re.compile("^[A-Za-z]+[\'-]?[A-Za-z]+")
        file_words = [words for line in f for words in line.split()
                if len(words) > 1 and word_pat.match(words)]
    return file_words

def wc_match(file_name):
    print Counter(match_list(file_name))

def wc(file_name):
    print Counter(create_list(file_name))

if __name__ == "__main__":
    file_name = 'test.txt'
    wc(file_name)
    wc_match(file_name)
