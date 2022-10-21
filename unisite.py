#爬取某网站高校对应网站
import requests
import random
import json
import socket

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
    'Cookie':"PHPSESSID=gljsd5c3ei5n813roo4878q203"}
    return headers


if __name__ == '__main__':

    school_id = []
    for i in range(1,8):
        requests2 = requests.get('https://api.eol.cn/web/api/?admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page='+str(i)+'&province_id=32&ranktype=&request_type=1&school_type=&size=20&top_school_id=[77,173,164]&type=&uri=apidata/api/gk/school/lists&signsafe=99cc3a645b6bad5e0040094a375cf7e8',headers=requests_headers()).json()
        for j in requests2['data']['item']:
            school_id.append(j['school_id'])
    print(school_id)

    site=[]
    test=requests.get('https://static-data.gaokao.cn/www/2.0/school/77/info.json',headers=requests_headers()).json()
    print(test)
    name=[]
    for i in range(len(school_id)):
        #url='https://static-data.gaokao.cn/www/2.0/school/77/info.json'
        requests3= requests.get("https://static-data.gaokao.cn/www/2.0/school/"+str(school_id[i])+"/info.json",headers=requests_headers()).json()
        name.append(requests3['data']['name'])
    for i in range(len(school_id)):
        #url='https://static-data.gaokao.cn/www/2.0/school/77/info.json'
        requests1= requests.get("https://static-data.gaokao.cn/www/2.0/school/"+str(school_id[i])+"/info.json",headers=requests_headers()).json()
        site.append(requests1['data']['school_site'])
    dic=dict(zip(name,site))
    for k in list(dic.keys()):
        if not dic[k]:
            del dic[k]
    with open('高校官网.txt', 'w') as f:
        for key in dic:
            f.write('\n')
            f.writelines('"' + str(key) + '": ' + str(dic[key]))
        f.write('\n')
