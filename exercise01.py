import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()

uname = input("请输入学生姓名:")
# mysql = ("select name,score from cls where name = '%s'"%name)
cur.execute("select name,score from cls where name = %s;",[uname])
for row in cur:
    print(row)


cur.close()
db.close()
