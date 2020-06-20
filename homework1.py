import pymysql
f = open("dict.txt")
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()
cur.execute("create database dict character set utf8;")
cur.execute("use dict;")
cur.execute("create table words(id int primary key auto_increment,word varchar(300),mean text);")
try:
    for line in f:
        list_line = line.split(" ",1)
        print(list_line)
        sql = "insert into words (word,mean) values (%s,%s)"
        mean = list_line[-1].replace("  ","")
        mean = mean.replace(r"\n","")
        if mean[0]==" ":
            mean = mean.replace(" ","",1)
        cur.execute(sql,[list_line[0],mean])
    db.commit()
except:
    db.rollback()
cur.close()
db.close()
f.close()
