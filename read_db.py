import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()

cur.execute('select * from cls;')  # 无返回值
# for row in cur:
#     print(row)
# row = cur.fetchone()
# print(row)
# row = cur.fetchmany(3)
# print(row)
row = cur.fetchall()
print(row)
cur.close()
db.close()
