#!/usr/bin/python  
#-*- coding:utf-8 -*-  
__author__ = "goodhe"

#=====================================

#File Name: mydict.py
#Mail: gdhe55555@gmail.com  
#Created Time: 2016-11-19 19:16:00

#=====================================


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
