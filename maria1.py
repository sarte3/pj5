import pymysql as my
import os

con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
cur = con.cursor()
sql = "insert into depdelay(yy, mm, cnt) values({}, {}, {})"

with open(os.path.join('F:\\', 'study', 'mapreduce', '1211', '2007.csv')) as f:
    for line in f.readlines():
        # print(line)
        data = line.split(',')
        # print(data[0])
        # print(data[1])
        # print(data[2].strip())
        cur.execute(sql.format(data[0], data[1], data[2].strip()))
    con.commit()
con.close()

