import pymysql
import json

db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='yournamedb')
cur=db.cursor()
sql='create table subscribe(id int,email varchar(30),status int,code varchar(30))'
cur.execute(sql)

id=[1,2,3,4,5,6,7,8]
email=['tom123@163.com','lucy123@163.com','lily123@163.com','jimmy123@163.com','joy123@163.com','zhangsan@163.com','lisi567@163.com','wenxiyun@163.com']
status=[1,None,0,0,1,0,0,1]
code=['TRBXPO','LOICPE','JIXDAMI','QKOLPH',None,'ZHANGS','LSIXNX','WENXIY']
sql='insert into subscribe values(%s,%s,%s,%s)'

for i in range(0,len(id)):
  cur.execute(sql,(id[i],email[i],status[i],code[i]))

db.commit() 
db.close()


