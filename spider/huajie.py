#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: huajie.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-12-07 17:05:55

#=====================================
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import time
import datetime
import pymysql

def getNowTime():
    return time.strftime("%Y-%m-%d %H:%M;%S", time.localtime(time.time()))

def filterLiveIds(url):
    html = urlopen(url)
    liveIds = set()
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.findAll("a", href=re.compile("^/l/")):
        if 'href' in link.attrs:
            newPage = link.attrs['href']
            liveId = re.findall("[0-9]+", newPage)
            liveIds.add(liveId[0])
    return liveIds

def getLiveIdsFromRecommendPage():
    liveIds = set()
    liveIds = filterLiveIds("http://www.huajiao.com/category/1000") | filterLiveIds("http://www.huajiao.com/category/1000?pageno=2")
    return liveIds

def getUserId(liveId):
    html = urlopen("http://www.huajiao.com/l/" + str(liveId))
    bsObj = BeautifulSoup(html, "html.parser")
    text = bsObj.get_text()
    res = re.findall("[0-9]+", text)
    return res[0]

def getUserData(userId):
    html = urlopen("http://www.huajiao.com/user/" + str(userId))
    bsObj = BeautifulSoup(html, "html.parser")
    data = dict()
    try:
        userInfoObj = bsObj.find("div", {"id":"userInfo"})
        data['FAvatar'] = userInfoObj.find("div", {"class":"avatar"}).img.attrs['src']
        userId = userInfoObj.find("p", {"class":"user_id"}).get_text()
        data['FUserId'] = re.findall("[0-9]+", userId)[0]
        tmp = userInfoObj.h3.get_text('|', strip=True).split('|')
        data['FUserName'] = tmp[0]
        data["FLevel"] = tmp[1]
        tmp = userInfoObj.find("ul", {"class":"clearfix"}).get_text('|', strip=True).split('|')
        data['FFollow'] = tmp[0]
        data['FFollowed'] = tmp[2]
        data['FSupported'] = tmp[4]
        data['FExperience'] = tmp[6]
        return data
    except AttributeError:
        print(str(userId) + ":html parse error in getUserData")
        return 0

def getUserLives(userId):
    try:
        url = "http://webh.huajiao.com/User/getUserFeeds?fmt=json&uid=" + str(userId)
        html = urlopen(url).read().decode('utf-8')
        jsonData = json.loads(html)
        print(jsonData)
        if jsonData['errno'] != 0:
            print(str(userId) + "error occured in getUserFeeds for: " + jsonData['msg'])
            return None

        return jsonData['data']['feeds']
    except Exception as e:
        print(e)
        return None

def getTimestamp():
    return (time.mktime(datetime.datetime.now().timetuple()))

def replaceUserLive(data):
    try:
        kvs = dict()
        kvs['FLiveId'] = int(data['relateid'])
        kvs['FUserId'] = int(data['FUserId'])
        kvs['FWatches'] = int(data['watches'])
        kvs['FPraises'] = int(data['praises'])
        kvs['FReposts'] = int(data['reposts'])
        kvs['FReplies'] = int(data['replies'])
        kvs['FPublishTimestamp'] = int(data['publishtimestamp'])
        kvs['FTitle'] = data['title']
        kvs['FImage'] = data['image']
        kvs['FLocation'] = data['location']
        kvs['FScrapedTime'] = getNowTime()
        Live().insert(kvs, 1)
    except pymysql.err.InternalError as e:
        print(e)

def spiderUserDatas():
    for liveId in getLiveIdsFromRecommendPage():
        userId = getUserId(liveId)
        userData = getUserData(liveId)
        if userData:
            User().insert(userData, 1)
    return 1

def spiderUserLives():
    userIds = User().select("FUserId").limit(100).fetchAll()
    for userId in userIds:
        liveDatas = getUserLives(userId[0])
        if liveDatas is not None:
            for liveData in liveDatas:
                liveData['feed']['FUserId'] = userId[0]
                replaceUserLive(liveData['feed'])

    return 1

class Mysql():
    def __new__(cls):
        cls.connect()
        return cls
    def __del__(cls):
        cls.close()

    @classmethod
    def connect(cls):
        #cls.conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='gdh', passwd='gdh', db='wanghong', charset='utf8')
        cls.conn = pymysql.connect(host='127.0.0.1', user='gdh', passwd='gdh', db='wanghong', charset='utf8')
        cls.cursor = cls.conn.cursor()
        cls.cursor.execute('set names utf8mb4')

    @classmethod
    def close():
        cls.cursor.close()
        cls.conn.close()

    @classmethod
    def query(cls, sql):
        cls.cursor.execute(sql)
        return cls

class Model():
    @classmethod
    def select(cls, selectStr):
        if selectStr.find(',') == -1:
            sqlFields = selectStr
        else:
            fields = list()
            for f in selectStr.split(','):
                fields.append('`' + f.strip() + '`')
            sqlFields = ','.join(fields)
        cls.sql = "SELECT " + sqlFields + " FROM " + cls.tb1
        return cls

    @classmethod
    def where(cls, string):
        cls.sql = cls.sql + " WHERE " + string
        return cls

    @classmethod
    def ordBy(cls, string):
        cls.sql = cls.sql + " ORDER BY " + string
        return cls

    @classmethod
    def limit(cls, num):
        cls.sql = cls.sql + " LIMIT " + str(num)
        return cls

    @classmethod
    def fetchAll(cls):
        return Mysql().query(cls.sql).cursor.fetchall()

    @classmethod
    def fetchOne(cls):
        return  Mysql().query(cls.sql).cursor.fetchone()

    @classmethod
    def insert(cls, data, replace=None):
        fields = list()
        for a in data.keys():
            fields.append('`' + a + '`')
        sqlFields = ','.join(fields)

        values = list()
        for v in data.values():
            v = "\"" + v + "\"" if type(v) is type("a") else str(v)
            values.append(v)
        sqlValues = ','.join(values)

        action = "INSERT" if replace is None else "REPLACE"
        sql = action + " INTO " + cls.tb1 + " (" + sqlFields + ") VALUES (" + sqlValues + ")"
        print(sql)
        Mysql().query(sql).conn.commit()

    @classmethod
    def update(cls, where, **data):
        pass

    @classmethod
    def delete(cls, where):
        sql = "DELETE FROM" + cls.tb1 + " WHERE " + where
        Mysql().query(sql).conn.commit()

class User(Model):
    tb1 = "Tbl_Huajiao_User"

class Live(Model):
    tb1 = "Tbl_Huajiao_Live"

def main(argv):
    if len(argv) < 2:
        print("Usage: python3 huajiao.py [spiderUserDatas|spiderUserLives]")
        exit()
    if(argv[1] == "spiderUserDatas"):
        spiderUserDatas()
    elif(argv[1] == "spiderUserLives"):
        spiderUserLives()
    elif(argv[1] == "getUserCount"):
        count = User().select("count(\"FUserId\")").fetchOne()
        print(count[0])
    elif(argv[1] == "getLiveCount"):
        count = Live().select("count(\"FLiveId\")").fetchOne()
        print(count[0])
    else:
        print("Usage: python3 huajiao.py [spiderUserDatas|spiderUserLives|getUserCount|getLiveCount]")

if __name__ == '__main__':
    main(sys.argv)
