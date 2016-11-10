#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0013.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-10 21:40:11

#=====================================
#0013:用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)

#import urllib2
from urllib import request
import os
from bs4 import BeautifulSoup

def get_img_src_list(url, img_class):
    content = request.urlopen(url).read()

    soup = BeautifulSoup(content, 'html.parser')

    src_list = []

    for img in soup.find_all('img', img_class):
        src_list.append(img['src'])

    return src_list

def download_img(src, download_path):
    print("Begin download image : %s" %src)

    file_name = src.split("/")[-1]

    dist = os.path.join(download_path, file_name)

    request.urlretrieve(src, dist, None)

    print("Download image %s Done." %src)

if __name__ == '__main__':
    src_list = get_img_src_list('http://tieba.baidu.com/p/2166231880', {"pic_type":"0"})
    if src_list:
        save_path = os.path.abspath("./download")
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        print("Start download %d images ...." % len(src_list))

        for src in src_list:
            download_img(src, save_path)

        print("Download %d images done." %len(src_list))

    else:
        print("No Images found!!!")

