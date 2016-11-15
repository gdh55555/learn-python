#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0019.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-15 22:37:45

#=====================================
'''第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
数字信息
-->
[
    [1, 82, 65535],
        [20, 90, 13],
            [26, 809, 1024]

]
</numbers>
</root>'''

import xlrd, codecs
from lxml import etree
from collections import OrderedDict

def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    #c = OrderedDict()
    c = {}
    for i in range(table.nrows):
        c[str(table.cell(i, 0).value)] = str(table.row_values(i)[1:])
    return c

def save_xml(data):
    output = codecs.open('numbers.xml','w', 'utf-8')
    root = etree.Element('root')
    numbers_xml = etree.ElementTree(root)
    numbers = etree.SubElement(root, 'numbers')
    numbers.append(etree.Comment("数字信息"))
    numbers.text = "\n" + str(data) + "\n"
    #sub = etree.SubElement(numbers, "num", data)
    #sub.tal = "\n"
    output.write(etree.tounicode(numbers_xml.getroot()))
    output.close()

if __name__ == "__main__":
    filename = 'numbers.xls'
    a = read_xls(filename)
    save_xml(a)
