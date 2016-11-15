#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0014.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-15 21:21:40

#=====================================
#纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）
import xlwt

with open("student.txt", "r") as f:
    content = f.read()

dic = eval(content)

file = xlwt.Workbook()
table = file.add_sheet('Test', cell_overwrite_ok=True)

def deal(key, value):
    table.write(int(key) -1, 0, key)
    for x in range(len(value)):
        #table.write(int(key)-1, x+1, str(value[x]).decode("gbk"))
        table.write(int(key)-1, x+1, str(value[x]))

for key, value in dic.items():
    deal(key, value)

file.save('student.xls')
