import requests
from bs4 import BeautifulSoup
import re
"""
爬取struts官网的漏洞对应cve
"""
if __name__ == '__main__':

    hdrs={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    for i in range (1,63):
        if i<10:
            url="https://cwiki.apache.org/confluence/display/WW/S2-00"+str(i)
        else :
            url = "https://cwiki.apache.org/confluence/display/WW/S2-0" + str(i)
        r = requests.get(url=url, headers=hdrs)
        soup = BeautifulSoup(r.content, "lxml")
        trs = soup.find_all('tr')
        for tr in trs:
            if "CVE Identifier" in tr.find('th').text:
                print("S2-00"+str(i)+":"+tr.find('td').text)
                break
        else:
            print("S2-0" + str(i) + ":" )


