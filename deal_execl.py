import pymysql
import xlrd
import xlwt
import re
import json
config={
    'host':'localhost',
    'port':3306,
    'db':'finger',
    'user':'root',
    'password':'123456',
    'charset':'utf8',
}
def read_vul():
    fingerp = []
    fingers = []
    finger = {}
    yunsee = []
    file1 = r'C:\Users\三岛semperfi\Desktop\LeanForGo\江苏学校官网指纹识别对比.xlsx'
    xlsx = xlrd.open_workbook(file1)
    table1 = xlsx.sheet_by_index(0)
    nrows = table1.nrows
    for i in range(1, nrows):
        if table1.cell_value(i, 0) != "":
            if i != 1:
                finger['fingerp'] = fingerp
                finger['yunsee'] = yunsee
                fingers.append(finger)
            fingerp = []
            yunsee = []

            finger['site'] = table1.cell_value(i, 0).split("http")[0].strip()
            finger['site'] = table1.cell_value(i, 0).split("http")[1].strip()
        if table1.cell_value(i, 1) != "": fingerp.append(table1.cell_value(i, 1))
        if table1.cell_value(i, 2) != "": yunsee.append(table1.cell_value(i, 2))
    return fingers

if __name__ == '__main__':

    content=read_vul()
    db=pymysql.connect(config)
    cursor=db.cursor()
    table_sql="CREATE TABLE `fingerprint_auto_task` (`id` int(11) NOT NULL AUTO_INCREMENT,`name` varchar(255) NOT NULL DEFAULT '' COMMENT '单位', `url` varchar(200) DEFAULT NULL COMMENT 'url',`fingerp_result` text COMMENT '数字观星指纹识别结果',`yunsee_result` text COMMENT '云悉指纹识别结果',`work_status` int(1) NOT NULL DEFAULT '0' COMMENT '数字观星0待下发，1识别结束，2识别超时',`site_type` varchar(10) NOT NULL DEFAULT '医院' COMMENT '站点类型',`yunsee_status` int(1) NOT NULL DEFAULT '0' COMMENT '云悉0待下发，1识别结束，2识别超时',PRIMARY KEY (`id`),KEY `fingername` (`name`)) ENGINE=InnoDB AUTO_INCREMENT=158 DEFAULT CHARSET=utf8;"
    cursor.execute(table_sql)
    db.commit()
    with open("content.txt",'w') as f:
        json.dump(content,f)