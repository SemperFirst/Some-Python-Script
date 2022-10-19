import re,os,random
import sqlite3
import time
from bs4 import BeautifulSoup as BS
import requests

pwd = os.getcwd()
rtitle=re.compile(r'title="(.*)"')
rbody=re.compile(r'body="(.*)')
rheader=re.compile(r'header="(.*)')

def requests_headers():
    user_agent = ['Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre',
                  'Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60',
                  'Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4062; en; U; ssr)',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']
    UA = random.choice(user_agent)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': UA,
        'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8',
        "Referer": "http://www.baidu.com/link?url=www.so.com&url=www.soso.com&&url=www.sogou.com",
        'Cookie': "PHPSESSID=gljsd5c3ei5n813roo4878q203"}
    return headers

#取出指纹数据库中id的结果
def check(_id):
    with sqlite3.connect(pwd+'/cms_finger.db') as conn:
        #创建游标
        cursor=conn.cursor()
        result=cursor.execute('SELECT name,keys FROM `tide` WHERE id=\'{}\''.format(_id))
        #取出id结果返回结果
        for row in result:
            return row[0],row[1]
def count():
    with sqlite3.connect(pwd+'/cms_finger.db') as conn:
        cursor=conn.cursor()
        result=cursor.execute('SELECT COUNT(id) FROM `tide`')
        for row in result:
            return row[0]
class Cmsscanner(object):
    def __init__(self,target):
        self.target=target
        self.start=time.time()
        self.finger=[]
    def get_info(self):
        """获取web信息"""
        try:
            r=requests.get(url=self,headers=requests_headers(),varify=False)
            content=r.text
            try:
                title=BS(content,'lxml').title.text.strip()
                return str(r.headers),content,title.strip('\n')
            except:
                return str(r.headers), content, ''
        except Exception as e:
            pass
    def check_rule(self,key,header,body,title):
        """指纹识别"""
        try:
            if 'title="' in key:
                if re.findall(rtitle,key)[0].lower() in title.lower():
                    return True
            elif 'body=' in key:
                    if re.findall(rbody,key)[0] in body: return  True
            else:
                    if re.findall(rheader,key)[0] in header: return  True
        except Exception as e:
            pass

    def  handle(self,_id,header,body,title):
        """取出数据库key匹配"""
        name,key=check(_id)
        #满足一个条件
        #只有一个条件
        #需要同时满足条件
