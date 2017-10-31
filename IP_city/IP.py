# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:03:00 2017

@author: Administrator
"""

import requests
from requests import Request, Session
from bs4 import BeautifulSoup
ips = ['123.151.77.71',
'113.96.219.248',
'123.151.77.123',
'183.3.255.28',
'123.151.77.72',
'14.116.133.171',
'123.151.77.90',
'113.96.218.50',
'183.3.227.102',
'110.156.236.210',
'223.114.16.170',
'123.151.77.123',
'123.151.77.70',
'61.148.244.197',
'183.30.187.0',
'117.136.79.85',
'14.126.226.93',
'123.151.77.73',
'39.86.54.78',
'125.39.45.236',
'60.8.153.231',
'123.151.77.70']
url = 'http://www.ip138.com/ips138.asp?ip=117.185.69.42&action=2' 

i= 0 
for item in ips:
    url = 'http://www.ip138.com/ips138.asp?ip=%s&action=2'%(item) 
    r = requests.get(url)
    if r.status_code == 200:
        
        s = BeautifulSoup(r.content, "lxml")
        area_raw = s.find('ul',class_="ul1")
        area = area_raw.text.split(' ')[0].split('：')[1]
        print ('第%d条 %s 地址是 %s'%(i , url , area))
    else:
        print ('第%d条 %s 地址无法查询'%(i, url ))
    i = i+1