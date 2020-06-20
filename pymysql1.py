import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'dict',
                     charset = 'utf8')
cur = db.cursor()




cur.close()
db.close()

