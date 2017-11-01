# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:03:00 2017

@author: Administrator
"""
'''
http://lbsyun.baidu.com/index.php?title=webapi/ip-api

使用的是web 服务api

'''
import requests
from requests import Request, Session
from bs4 import BeautifulSoup
import pymysql 
import json
conn = pymysql.connect(host = 'localhost', 
                       user = 'root' ,
                       password = '1987', 
                       db = 'ip',
                       charset='utf8')

cursor = conn.cursor()
sql = '''
select c.clueregsid, c.cf_4038
from ec_clueregs c 
where (c.city_web_info is null 
or c.city_web_info  ='')
and c.cf_4038 is not null 
'''

cursor.execute(sql)
ips =cursor.fetchall()


#url = 'http://api.map.baidu.com/location/ip?ip=123.151.77.71&ak=AE4be5b5107fcec99136904e7b81e948&coor=bd09ll'
#r = requests.get(url)
#data = json.loads(r.content)
#city = data['content']['address_detail']['city']


#i= 0 
for item in ips:
    ip = item[1]
    url = 'http://api.map.baidu.com/location/ip?ip=%s&ak=AE4be5b5107fcec99136904e7b81e948&coor=bd09ll'%(ip) 
    r = requests.get(url)
    if r.status_code == 200:    
        try:
            data = json.loads(r.content)
            city = data['content']['address_detail']['city']
            update = '''
            update ec_clueregs 
            set city_web_info = '%s'
            where clueregsid = '%d'
        
            '''%(city , item[0])
            cursor.execute(update)
            cursor.execute('commit')
        except:
            print ('%s 没有查询成功'%(ip))

    else:
        print ('%s 没有查询成功'%(ip))
