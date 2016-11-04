#!/usr/bin/python
# -*- coding: utf-8 -*-

# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# Require to put them in the same directory.
# iPhone5 Resoulution:1136x640

import os
from PIL import Image

def resize_image(image):
    im = Image.open(image)
    width, height= im.size
    if height > 1136 or width > 640:
        th = height / 1136
        td = width / 640
        ts = max(th, td)
        nh = height / ts
        nw = width / ts
        im = im.resize((nw, nh))
        im.save(image)
        print 'Suc1cessfully resized %s. New width is %i, new height is %i.' % (image, nh, nw)
    else:
        print "There's no need to resize %s." % image

def main():
    for i in os.listdir("img"):
        try:
            resize_image(os.path.join("img", i))
        except IOError:
            print "Ooops! %s is not supported to make the change!" %i

if __name__ == "__main__":
    main()
