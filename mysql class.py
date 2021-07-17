class Mysql_connect:

  def __init__(self,table_name):
      self.table_name = table_name
      self.database = 'db'
  
  def connent_database(self):
      db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='{self.database}')
      cur=db.cursor()
      return cur

  def create_table(self):
      sql='create table {self.table_name}(rank int,title varchar(250),link varchar(255))'
      cur.execute(sql)

  def update_table(self,sql,args,cur):
      result = cur.execute(sql,args)
      print(result)
      db.commit()
      cur.close()

  def insert_data(self,cur,rank,title,link):
      sql='insert into grade values(%s,%s,%s)'
      cur.execute(sql,(rank,title,link))

  def del_table(self,cur):
      sql='drop table {self.talbe}'
      cur.execute(sql)