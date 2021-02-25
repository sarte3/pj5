import pymysql as my
import os

con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
cur = con.cursor()
sql = "insert into daydelay(dow, cnt) values('{}', {})"

with open('f:\\study\\mapreduce\\1211\\leejeongsam.txt') as f:
    for line in f.readlines():
        data = line.split('\t')
        cur.execute(sql.format(data[0], data[1].strip()))
    con.commit()
con.close()
