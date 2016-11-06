#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0010-1.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-06 22:15:22

#=====================================

import Image, ImageDraw, ImageFont, ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色
def rndColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32, 127))

def generateImg():
    width = 60*4
    height = 60
    image = Image.new("RGB", (width, height), (255,255,255))
    font = ImageFont.truetype("arial.ttf", 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for t in range(4):
        draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())

    image = image.filter(ImageFilter.BLUR)
    image.save("code.jpg")

if __name__ == "__main__":
    generateImg()

