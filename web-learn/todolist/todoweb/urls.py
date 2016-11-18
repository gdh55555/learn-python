#!/usr/bin/python  
#-*- coding:utf-8 -*-  
__author__ = "goodhe"

#=====================================

#File Name: urls.py
#Mail: gdhe55555@gmail.com  
#Created Time: 2016-11-18 16:28:04

#=====================================

from django.conf.urls import url
from todoweb import views

urlpatterns = [
        url('', views.index, name='index'),
        url(r'^$', views.index, name='index'),
        ]
