import pymysql
#连接数据库
conn=pymysql.connect('localhost',user="root",passwd="",db="pythontest")

try:
    #创建游标
    cur=conn.cursor()
    #创建数据库
    #cur.execute('CREATE DATABASE PythonTest')
    #print('数据库创成功')
    #创建表
    cur.execute('drop table if exists user')
    sql="""CREATE TABLE IF NOT EXISTS `user`(
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `age` int(11) NOT NULL,
        PRIMARY KEY(`id`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
    cur.execute(sql)
    insert=cur.execute("insert into user values(1,'tom',18)")
    #另一种插入数据方式 通过字符串传入
    sql="insert into user values(%s,%s,%s)"
    cur.execute(sql,(2,'jimmy',20))
    print('插入数据执行成功')
    #批量插入数据
    sql="insert into user values(%s,%s,%s)"
    cur.executemany(sql,[(4,'wen',16),(3,'xiaohu',22),(7,'knight',21)])
    print('批量数据插入成功')
    #查询数据
    sql="select * from user"
    cur.execute(sql)
    print(cur.rownumber)
    print(cur.rowcount)
    print('删除数据前数据库为')
    result=cur.fetchone()
    while result!=None:
        print(result,cur.rownumber)
        result=cur.fetchone()
    #删除数据
    sql="delete from user where id=%s"
    cur.executemany(sql,[(3),(4)])
    print('删除数据后')
    cur.execute('select * from user')
    for r in cur.fetchall():
        print(r)
    
    #关闭游标
    cur.close()
    conn.commit()
    #关闭数据库连接
    conn.close()

except pymysql.err.MySQLError as _error:
    print('错误异常')
    raise _error






