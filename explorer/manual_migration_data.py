# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:40:47 2017

@author: Administrator
"""

import pymysql 
import pandas as pd 
conn1 = pymysql.connect('192.168.0.54','masg','yixue123','yixue')
conn2 = pymysql.connect('localhost','root','1987','yixue')

#获取全部表的名字
sql1 = 'show tables'
cursor1 = conn1.cursor()
cursor1.execute(sql1)
tables = cursor1.fetchall()

#导入
for t in tables :
    print (t[0])
    print ('select * from %s'%(t[0]))
    df = pd.read_sql_query('select * from %s'%(t[0]) ,conn1)
    df.to_sql('t[0]',conn2 ,if_exists='replace' )
    