import random
import re
import json
import pymysql
import requests
import lxml
from bs4 import BeautifulSoup
import html5lib
config={
    'host':'localhost',
    'port':3306,
    'db':'finger',
    'user':'root',
    'password':'123456',
    'charset':'utf8',
}
def requests_headers():
    user_agent = ['Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre',
    'Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60','Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4062; en; U; ssr)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']
    UA = random.choice(user_agent)
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent':UA,
    'Upgrade-Insecure-Requests':'1','Connection':'keep-alive','Cache-Control':'max-age=0',
    'Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8',
    "Referer": "http://www.baidu.com/link?url=www.so.com&url=www.soso.com&&url=www.sogou.com",
    'cookie':'user=%7B%22loginTime%22%3A1666262157254%2C%22token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZGRUaW1lIjoxNjY2MjYyMTU3MjU0LCJlbWFpbCI6IjM3MzA1MjQyM0BxcS5jb20ifQ.dI4Wj1H3Hi6CurVWz9enaaFb2yDZpANt_BQz2oGEs7Q%22%2C%22user%22%3A%7B%22activate%22%3A0%2C%22certNumber%22%3A%22%22%2C%22detection%22%3A10%2C%22email%22%3A%22373052423%40qq.com%22%2C%22fingerIntegral%22%3A0.00%2C%22fingerprintNum%22%3A0%2C%22id%22%3A2906%2C%22integral%22%3A0.00%2C%22issueAvailable%22%3A0%2C%22issueTotal%22%3A0%2C%22level%22%3A1%2C%22loginTime%22%3A1665561447000%2C%22nickname%22%3A%22%E6%B2%B9%E7%82%B8%E9%B8%A1%E7%B1%B3%E8%8A%B1%22%2C%22pocAvailable%22%3A0%2C%22pocIntegral%22%3A0.00%2C%22pocTotal%22%3A0%2C%22pocTotalIntegral%22%3A0.00%2C%22portrait%22%3A%22%22%2C%22rangeAvailable%22%3A0%2C%22rangeTotal%22%3A0%2C%22thirdPartyId%22%3A0%2C%22totalFingerIntegral%22%3A0.00%2C%22totalIntegral%22%3A0.00%7D%7D'  ,'Content-Type':'application/json'
}
    return headers


if __name__ == '__main__':

    name = []
    website = []
    data = {"pageBasic": {"pageNum":1, "numPerPage": 10},
            "appInfoWhere": {"likeName": None, "category": None, "searchType": 0}}
    url = 'https://fp.shuziguanxing.com/fp/appInfo/repertory'
    res = requests.post(url=url, headers=requests_headers(), data=json.dumps(data)).text
    context = json.loads(res)
    for result in context['info']['result']:
        name.append(result['name'])
        website.append(result['website'])
    dic=dict(zip(name,website))
    print(dic)

""""
    网页内容前后端分离需要抓取api解析
    soup=BeautifulSoup(html,"html.parser")
    print(soup.prettify())
    #找到网页的表格
    table=soup.find('table', {'class':''})
    #找到表格有多少行
    results=table.find_all('tr')
    #取每一行数据
    for result in results:
        data=result.find_all('td')
        name=data[0].getText()
        kind=data[1].getText()
        company=data[2].getText()
        discrib=data[3].getText()
        rows.append([data,name,kind,company,discrib])
    print(rows)
"""