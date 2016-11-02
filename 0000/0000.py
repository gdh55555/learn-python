#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'goodhe'

#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def imageWriter(filePath, number = 1):
    img = Image.open(filePath)
    size = img.size
    # set the font size
    fontSize = size[1] // 4
    draw = ImageDraw.Draw(img)
    # create a font instance
    ttFont = ImageFont.truetype("arial.ttf", fontSize)
    draw.text((size[0]-fontSize, 0), str(number), fill=(255,67,0), font=ttFont)
    img.show()
    img.save("2.bmp")

#print imageWriter("test.jpg")
imageWriter("1.bmp")
