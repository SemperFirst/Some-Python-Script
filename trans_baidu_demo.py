# -*- coding: utf-8 -*-
import logging
import time

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import random
import json
import hashlib
import requests
import pymysql

class trans_baidu_demo:
    def __init__(self):
        self.url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
        self.headers = {
            "Referer": "https://api.fanyi.baidu.com",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # Set your own appid/appkey.
        self.appid = '20221013001390820'
        self.appkey = 'QaauYH2crzb8xL2_KMIw'

    def get_md5(self, sign):
        md5 = hashlib.md5()
        md5.update(sign.encode("utf-8"))   # 需要一个bytes格式的参数
        return md5.hexdigest()

    def get_salt(self):
        salt = random.randint(32768, 65536)
        return salt

    def get_sign(self, content, salt):
        complete_sign = self.appid + content + str(salt) + self.appkey
        md5sign = self.get_md5(complete_sign)
        return md5sign

    def http_post_retry(self, payload):
        count = 0
        while count < 5:
            try:
                # Send request
                r = requests.post(
                    self.url,
                    params=payload,
                    headers=self.headers
                )
                if r.status_code == 200 or r.status_code == 404 or r.status_code == 403:
                    return r
            except:
                time.sleep(0.8)
                count += 1
        logging.warning("http_get_retry() failed 5 times in url: ")

    def trans_to_en(self, content):
        from_lang = 'zh'
        to_lang = 'en'
        salt = self.get_salt()
        payload = {
            'appid': self.appid,
            'q': content,
            'from': from_lang,
            'to': to_lang,
            'salt': str(salt),
            'sign': self.get_sign(content, salt)
        }
        r = self.http_post_retry(payload)
        if r.text[0] != "{":
            return ""
        res = json.loads(r.text)

        if res['trans_result'] != "":
            data = ""
            num = len(res['trans_result'])
            for result in res['trans_result']:
                num -= 1
                symbol = ""
                a = symbol.join(result['dst'])
                if num > 0:
                    data = data + a + "\n"
                else:
                    data = data + a
            return data
        else:
            print(r.text)
            return ""

    def trans_to_cn(self, content):
        from_lang = 'en'
        to_lang = 'zh'
        salt = self.get_salt()
        payload = {
            'appid': self.appid,
            'q': content,
            'from': from_lang,
            'to': to_lang,
            'salt': str(salt),
            'sign': self.get_sign(content, salt)
        }

        # result = r.json()
        # print(json.dumps(result, indent=4, ensure_ascii=False))
        # res = json.loads(r.text)
        # #print(res['trans_result'][0]['dst'])
        r = self.http_post_retry(payload)
        if r.text[0] != "{":
            return ""
        res = json.loads(r.text)
        if res['trans_result'] != "":
            data = ""
            num = len(res['trans_result'])
            for result in res['trans_result']:
                num -= 1
                symbol = ""
                a = symbol.join(result['dst'])
                if num > 0:
                    data = data + a + "\n"
                else:
                    data = data + a
            return data
        else:
            print(r.text)
            return ""

    def check(self):
        result = self.trans_to_en("你好，世界\n你好")
        if "Hello" in result:
            return True
        else:
            return False


def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


if __name__ == "__main__":

    conn = pymysql.connect()
    cursor = conn.cursor()

    sql = "select  * from product_fingerprint where  length(product_name_en)!=char_length(product_name_en) or product_name_en=''"
    cursor.execute(sql)
    rows = cursor.fetchall()
    a=trans_baidu_demo()
    for row in rows:
        product_name_cn = row['product_name_cn']
        product_name_en_new = a.trans_to_en(product_name_cn)
        if product_name_en_new!=product_name_cn:
            print(product_name_en_new)
            sql = "UPDATE product_fingerprint SET product_name_en_new=%s,status_en=%s WHERE id=%s"
            cursor.execute(sql, (product_name_en_new,1, row['id']))
        if product_name_en_new == product_name_cn:
            sql = "UPDATE product_fingerprint SET product_name_en_new=%s,status_en=%s WHERE id=%s"
            cursor.execute(sql, ('', 0, row['id']))
    conn.commit()
    cursor.close()
    conn.close()
