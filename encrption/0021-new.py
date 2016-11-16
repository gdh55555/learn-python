#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: 0021.py
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-16 08:49:29

#=====================================

#通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

import uuid
import hashlib
#from collection import defaultdict

db = {}
#db = defualtdict(lambda: 'N/A')

def hash_passwd(password):
    salt =  uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

def check_passwd(hashed_passwd, user_passwd):
    passwd, salt = hashed_passwd.split(":")
    return passwd == hashlib.sha256(salt.encode() + user_passwd.encode()).hexdigest()

def register(username, password):
    if db.get(username) != None:
        print("You have register!!")
    else:
        db[username] = hash_passwd(password)

def login(username, password):
    if db.get(username) == None:
        print("You have not registered!!")
    else:
        hashed = db.get(username)
        if(check_passwd(hashed, password)):
            print("Login success!!")
        else:
            print("You have wrong password!!")

while True:
    new_user = input("Please enter a username: ")
    new_pass = input("Please enter a passwd: ")
    register(new_user, new_pass)
    old_user = input("Now please enter the user again to login: ")
    old_pass = input("Now please enter the password again to login: ")
    login(old_user, old_pass)
