# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:03:00 2017

@author: Administrator
"""

import requests
from requests import Request, Session
from bs4 import BeautifulSoup
import pymysql 
conn = pymysql.connect(host = 'localhost', 
                       user = 'root' ,
                       password = '1987', 
                       db = 'ip',
                       charset='utf8')

cursor = conn.cursor()
sql = '''
select c.clueregsid, c.cf_4038
from ec_clueregs c 
where c.city_web_info is null 
and c.cf_4038 is not null 
'''

cursor.execute(sql)
ips =cursor.fetchall()

#url = 'http://www.ip138.com/ips138.asp?ip=117.185.69.42&action=2' 

i= 0 
for item in ips:
    ip = item[1]
    url = 'http://www.ip138.com/ips138.asp?ip=%s&action=2'%(ip) 
    r = requests.get(url)
    if r.status_code == 200:     
        s = BeautifulSoup(r.content, "lxml")
        try:
            area_raw = s.find('ul',class_="ul1")
            area = area_raw.text.split(' ')[0].split('：')[1]
#            print ('第%d条 %s 地址是 %s'%(i , url , area))
            update = '''
            update ec_clueregs 
            set city_web_info = '%s'
            where clueregsid = '%d'
        
            '''%(area , item[0])
            cursor.execute(update)
            cursor.execute('commit')
        except Exception as e :
            pass
    else:
#        print ('第%d条 %s 地址无法查询'%(i, url ))
    i = i+1