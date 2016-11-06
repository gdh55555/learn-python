#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0010.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-06 21:40:11

#=====================================
#使用 Python 生成类似于下图中的字母验证码图片
from random import choice
import string
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

def generateRandomLetters():
    return ''.join([choice(string.ascii_uppercase) for x in range(4)])

def createVerifyImg(str):
    img = Image.new('RGB', (240,60), (255,255,255))
    font = ImageFont.truetype('DejaVuSansMono.ttf', 36)
    draw = ImageDraw.Draw(img)

    for x in range(240):
        for y in range(60):
            draw.point((x,y), tuple([choice(range(128,255)) for color in range(3)]))

    for x in range(len(str)):
        draw.text((60*x+10, 10), str[x], tuple([choice(range(32, 127)) for color in range(3)]), font)

    img = img.filter(ImageFilter.BLUR)
    return img

if __name__ == "__main__":
    img = createVerifyImg(generateRandomLetters())
    img.save("verifyImg.jpg")
