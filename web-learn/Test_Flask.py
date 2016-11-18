#!/usr/bin/python  
#-*- coding:utf-8 -*-  
__author__ = "goodhe"

#=====================================

#File Name: testflask.py
#Mail: gdhe55555@gmail.com  
#Created Time: 2016-11-18 10:52:03

#=====================================

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run()
