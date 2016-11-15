#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0017.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-15 21:48:15

#=====================================
#将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中

import xlrd, re, json
import sys

#sys.reload()
#sys.setdefaultencoding("utf-8")

with xlrd.open_workbook("student.xls") as f:
    table = f.sheet_by_index(0)

rows = table.nrows
cols = table.ncols

dic = {}

content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<student>\n<!--\n     学生信息表\n   "id" : [名字, 数学, 语文, 英文]\n-->\n'

for row in range(rows):
    stu = table.row_values(row)
    lists = []
    for x in range(len(stu)-1):
        lists.append(stu[x+1])
    dic[stu[0]] = lists

#s = json.dumps(dic, indent=4, ensure_ascii=False)
s = json.dumps(dic, indent = 4, ensure_ascii=False)

content = content + s + '\n</students>\n</root>'
with open('student.xml', 'w') as f:
    f.write(content)
