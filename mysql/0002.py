#!/usr/bin/python 
# -*-coding:utf-8 -*-

# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import MySQLdb
import string
import random

def base_str():
    return (string.letters + string.digits)

def key_gen(KeyLen = 20):
    keylist = [random.choice(base_str()) for i in range(KeyLen)]
    return ("".join(keylist))

def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(str(key_gen()))
    return result

class mysql_init(object):

    def __init__(self, conn):
        self.conn = None

    #connect to MySQL
    def connect(self):
        self.conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user="gudh",
                passwd="gdh",
                db="test",
                )
                #charset="utf-8"
    
    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect();
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()

def process():
    dbconn.connect()
    conn = dbconn.cursor()
    #DropTable(conn)
    #CreateTable(conn)
    #InsertDatas(conn)
    DeleteData(conn)
    QueryData(conn)
    conn.close()          #close cursor
    dbconn.commit()       #commit Operation
    dbconn.close()        #close dbcon
    
def query(sql, conn):
    '''查询sql'''
    conn.execute(sql)
    rows = conn.fetchall()
    return rows

def DropTable(conn):
    conn.execute("DROP TABLE IF EXISTS `user_key`")

def CreateTable(conn):
    sql_create = '''CREATE TABLE `user_key` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `key` varchar(50) NOT NULL)'''
    conn.execute(sql_create)

def InsertDatas(conn):
    insert_sql = "INSERT INTO user_key (`key`) VALUES (%(value)s)"
    key_list = key_num(200);
    conn.executemany(insert_sql, [dict(value=v) for v in key_list])

def DeleteData(conn):
    del_sql = "DELETE FROM user_key where id=2"
    conn.execute(del_sql)

def QueryData(conn):
    sql = "SELECT * FROM user_key"
    rows = query(sql, conn)
    printResult(rows)

def printResult(rows):
    if rows is None:
        print "rows None"
    for row in rows:
        print row

if __name__ == "__main__":
    dbconn = mysql_init(None)
    process()
