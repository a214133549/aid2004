"""
1. 将dict.txt中点单词存入到数据库
 创建一个数据库  dict
 create database dict charset=utf8;
 创建数据表     words  字段： id   word   mean
 create table words (
 id int primary key auto_increment,
 word varchar(30),
 mean varchar(512));
 将单词本中单词插入到这个数据表
"""

import pymysql
import re

# 连接数据库 (连接本机数据库host port 可以不写)
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "dict",
                     charset = "utf8")

# 创建游标   （游标：对数据库进行数据操作的对象，可以获取操作结果）
cur = db.cursor()

# 将单词表中内容插入数据库
f = open('dict.txt')
l = []

sql = "insert into words (word,mean) values (%s,%s);"
try:
    for line in f:
        a = re.findall(r"(\w+)\s+(.*)",line) # 匹配出单词和解释
        # l[0] ---> (word,mean)
        l.append(a[0])
    cur.executemany(sql,l)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库
f.close()
cur.close()
db.close()