#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: demo3.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-22 22:29:37

#=====================================

def process_student(name):
    std = Student(name)
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_1(std)
    do_subtask_2(std)


