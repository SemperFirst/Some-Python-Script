import re
import pymysql
def capitalize_exprname(str):
    arry = []
    arry = str.split()
    result=""
    for word in arry:
        if word.upper() in proname:
            result+=(word.upper() + " ")
        else:
            result+=word.capitalize()+" "
    return result
if __name__ == '__main__':
    proname=[]
    arry=[]
    with open("proname.txt", "r", encoding="UTF-8") as f:
        lines=f.readlines()
        for line in lines:
            line=re.sub(r'\n','',line)
            proname.append(line)

    conn = pymysql.connect(host='10.50.24.152', port=3308, user='root', passwd='bdwOgW5p1dUfyINu', db='fingerprint_feature', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor()
    try:
        sql="SELECT * FROM web_fingerprint_item "
        cursor.execute(sql)
        rows=cursor.fetchall()
        for row in rows:
            fingerprint_name_new=capitalize_exprname(row['fingerprint_name'])
            sql = "UPDATE web_fingerprint_item SET fingerprint_name_new=%s,fingerpring_status=1 WHERE id=%d"
            cursor.execute(sql, (fingerprint_name_new,row['id']))
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()


