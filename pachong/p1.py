import requests
from bs4 import BeautifulSoup
hdrs={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url="http://html-color-codes.info/color-names/"
r=requests.get(url=url,headers=hdrs)
soup=BeautifulSoup(r.content, "lxml")

#print(soup.prettify())

print(soup.title.string)
trs=soup.find_all('tr')
for tr in trs:
    style=tr.get('style')
    tds=tr.find_all('td')
    td=[x for x in tds]
    name=td[1].text
    hex=td[2].text
    print('颜色：%-20s值：%-20s样式：%-20s'%(name,hex,style))
