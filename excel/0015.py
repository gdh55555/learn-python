#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0015.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-15 21:35:15

#=====================================

#纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）
import xlwt

with open("city.txt", "r") as f:
    content = f.read()

dic = eval(content)

file = xlwt.Workbook()
table = file.add_sheet("city")

def deal(key, value):
    table.write(int(key)-1, 0, key)
    table.write(int(key)-1, 1, str(value))

for key, value in dic.items():
    deal(key, value)

file.save("city.xls")


