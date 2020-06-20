import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()


try:
    sql = "insert into cls values (10,'tony','19','m',85)"
    cur.execute(sql)
    db.commit()
except:
    print("输入有误")
    db.rollback()



cur.close()
db.close()
