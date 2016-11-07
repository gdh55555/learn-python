#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0012.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-07 14:56:55

#=====================================

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
        inputWord = raw_input("input your lines>>>")
        for word in filteredwords:
            if word in inputWord:
                #inputWord = inputWord.replace(word, '*'*len(word))
                inputWord = inputWord.replace(word, ''.join(['*' for x in range(len(word))]))
        print inputWord

