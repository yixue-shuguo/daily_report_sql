# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:03:00 2017

@author: Administrator
"""

import requests
from requests import Request, Session
from bs4 import BeautifulSoup
ips = ['123.151.76.248',
'59.35.160.81',
'61.151.178.175',
'61.151.178.176',
'123.151.77.121',
'113.96.219.243',
'123.151.77.71',
'182.135.8.140',
'14.116.133.171',
'123.151.77.121',
'14.116.137.167',
'125.39.45.236',
'223.104.64.62',
'123.151.77.121',
'36.98.83.66',
'27.213.53.105',
'125.39.46.47',
'60.10.185.29',
'183.25.193.23',
'124.238.223.181',
'110.243.185.255',
'183.196.55.251',
'124.237.48.56']
url = 'http://www.ip138.com/ips138.asp?ip=117.185.69.42&action=2' 


for item in ips:
    url = 'http://www.ip138.com/ips138.asp?ip=%s&action=2'%(item) 
    r = requests.get(url)
    if r.status_code == 200:
        
        s = BeautifulSoup(r.content, "lxml")
        area_raw = s.find('ul',class_="ul1")
        area = area_raw.text.split(' ')[0].split('：')[1]
        print ('%s 地址是 %s'%(url , area))
    else:
        print ('%s 地址无法查询'%(url ))