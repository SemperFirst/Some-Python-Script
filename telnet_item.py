import re
import pymysql

def get_data(cursor):
    sql="select * from sumap_protocol"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
def deal(content):
    list=['Command line is locked now, please retry later.','But One connection() already keep alive.',"%connection closed by remote host!"]
    content = content.encode('ISO-8859-1','ignore').decode('utf-8','ignore')
    # 利用正则匹配\x开头的特殊字符
    zifu = re.findall(r'\\x[A-Z0-9]{2}', content)
    for x in zifu:
        # 替换找的的特殊字符
        content = content.replace(x, '')
    # 最后再解码
    content = content.replace("#", '').replace('User Access Verification','').replace('Login authentication','').replace('Login as: ','').replace('HOSTNAME login:','').replace('login:','').replace('Username:','').replace('!','').replace('$','').replace('User:','').replace('\"','').replace('\'','').replace('Password:','').replace('>>User name:','').replace('Login:','').strip()
    content = content.encode('utf-8','ignore').decode('ISO-8859-1','ignore')
    if content in list:
        content=""
    return content

if __name__ == '__main__':

    conn = pymysql.connect()
    cursor = conn.cursor()
    rows=get_data(cursor)
    for row in rows:
        banner=row['banner']
        result=deal(banner)
        print(result)
        sql = "update sumap_protocol set result = %s where id = %s"
        arg = (result,row['id'])
        cursor.execute(sql,arg)
    conn.commit()
    cursor.close()
    conn.close()

