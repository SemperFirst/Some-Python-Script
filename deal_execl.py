import pymysql
import xlrd
import xlwt
import re
import json

def read_vul():

    fingers = []
    fingerp = []
    yunsee = []
    finger={}
    file1 = r'江苏学校官网指纹识别对比.xlsx'
    xlsx = xlrd.open_workbook(file1)
    table = xlsx.sheet_by_index(0)
    rows = table.nrows
    fingers = []
    fingerp = []
    yunsee = []
    finger = {}
    for i in range(1, rows):
        if table.cell_value(i, 0) != "":
            if i != 1:
                finger["fingerp"] = fingerp
                finger["yunsee"] = yunsee
                fingers.append(finger)
                finger = {}
            fingerp = []
            yunsee = []
            # print(table.cell_value(i,0).split("http")[0].strip())
            finger["name"] = table.cell_value(i, 0).split("http")[0].strip()
            finger["url"] = "http" + table.cell_value(i, 0).split("http")[1].strip()
        if table.cell_value(i, 1) != "":
            fingerp.append(table.cell_value(i, 1))
        if table.cell_value(i, 2) != "":
            yunsee.append(table.cell_value(i, 2))
    return fingers
if __name__ == '__main__':

    content=read_vul()
    print(content)
    db=pymysql.connect('localhost',user="root",passwd="123456",db="finger_auto")
    cursor=db.cursor()
    for i in range(len(content)):
        name=content[i].get('name')
        url=content[i].get('url')
        yunsee_result=str(content[i].get('yunsee'))
        fingerp_result=str(content[i].get('fingerp'))
        try:
            cursor.execute("INSERT INTO fingerprint_auto_task (name,url,fingerp_result,yunsee_result)values(%s,%s,%s,%s)",(name,url,fingerp_result,yunsee_result))
            db.commit()
        except Exception as err:
            db.rollback()
    cursor.close()
    db.close()