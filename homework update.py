import pymysql
import json

db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='yournamedb')
cur=db.cursor()

def update(sql,args):
    cur = db.cursor()
    result = cur.execute(sql,args)
    print(result)
    db.commit()
    cur.close()


if __name__ == '__main__':
    sql = 'UPDATE subscribe SET code=%s WHERE id = %s;'
    args = ('AAABBB', 4)
    update(sql, args)
    sql = 'UPDATE subscribe SET status = %s WHERE email = %s;'
    args = ('1', 'lisi567@163.com')
    update(sql, args)  
    sql = 'DELETE FROM subscribe WHERE id = %s;'
    args = ('5',)


