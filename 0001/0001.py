#!/usr/bin/env python       
# -*- coding: utf-8 -*-
__author__ = "goodhe"

# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激>活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

from random import Random
import uuid

def codeGenarator(number, codeLength = 8):
    print '*****   Code Genarator *****'
    codeFile = open('codes.text', 'w')
    if number <= 0:
        codeFile.close();
        return 'invalid number of codes'
    else:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        random = Random()
        for i in range(1, number+1):
            str = ''
            for j in range(1, codeLength+1):
                index = random.randint(1, len(chars))
                str += chars[index-1]
                #是否需要判断重复
            codeFile.write(str + '\n');
    codeFile.close();

def uuidGenarator(number):
    uuids = []
    for i in range(number):
        uuids.append(uuid.uuid1())
    print uuids

print codeGenarator(200);
uuidGenarator(20)

