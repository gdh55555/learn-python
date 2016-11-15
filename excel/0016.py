#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0016.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-15 21:43:25

#=====================================

#纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

import xlwt

with open("numbers.txt", "r") as f:
    content = f.read()
lists = eval(content)

file = xlwt.Workbook()
table = file.add_sheet("numbers")

for row in range(len(lists)):
    for col in range(len(lists[row])):
        table.write(row, col, lists[row][col])

file.save("numbers.xls")

