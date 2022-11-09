import pymysql
import json
import os
import re
#将json格式文件存入数据库
class SumapData:
    def __init__(self):

        self.port = 3308
        self.host = '10.50.24.152'
        self.user = 'root'
        self.passwd = 'bdwOgW5p1dUfyINu'
        self.db = 'fingerprint_feature'
        self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset='utf8mb4',cursorclass = pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def parse_json(self, json_file):
        sumap_datas = []
        with open(json_file,'r',encoding='UTF-8') as f:
            lines = f.readlines()
            for line in lines:
                sumap_data = json.loads(line)
                banner = sumap_data["data"]
                ip = sumap_data["ip"]
                protocol = "telnet"
                port = sumap_data["port"]
                sumap_datas.append((banner, ip, protocol, port))
        return sumap_datas


    def insert_db(self, sumap_datas):
        sql = "insert sumap_protocol(banner, ip, protocol, port) values(%s,%s,%s,%s)"
        self.cur.executemany(sql, sumap_datas)
        self.conn.commit()


    def main(self):
        path = os.getcwd() + '/data20221108'
        for fpath, dirname, fnames in os.walk(path):
            for json_file in fnames:
                if '.json' in json_file:
                    sumap_datas = self.parse_json('data20221108/' + json_file)
                    self.insert_db(sumap_datas)


if __name__ == '__main__':
    
    SumapData().main()






