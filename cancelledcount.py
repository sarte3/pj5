import pymysql as my
import os

con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
cur = con.cursor()
sql = "insert into cancelled(yy, mm, cnt) values({}, {}, {})"

with open('f:\\study\\mapreduce\\1215\\resultCancelled2007.txt') as f:
    for line in f.readlines():
        data = line.split(',')
        cur.execute(sql.format(data[0], data[1], data[2].strip()))
    con.commit()
con.close()
