import pymysql
import json

db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='db')
cur=db.cursor()
sql='create table grade(id varchar(10),name varchar(10),age int,score int,class varchar(10))'
cur.execute(sql)

#id=['101','102','103','104','105','106','107','108','109','110']
f = open('id.json','r')
id = json.load(f)
name=['诸葛亮','刘备','周瑜','张飞','关羽','吕布','貂蝉','黄忠','马超','典韦']
age=[28,30,27,26,28,28,24,26,23,18]
score=[89,56,78,60,40,33,90,95,86,82]
class_=['一班','一班','一班','二班','二班','二班','三班','三班','三班','三班']
sql='insert into grade values(%s,%s,%s,%s,%s)'

for i in range(0,len(id)):
  cur.execute(sql,(id[i],name[i],age[i],score[i],class_[i]))

db.commit() 
db.close()



