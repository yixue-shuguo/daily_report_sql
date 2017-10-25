# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:57:03 2017

@author: Administrator
"""

import pymysql 

conn = pymysql.connect('rr-uf647q511648367cso.mysql.rds.aliyuncs.com','crm_root','Hello2017','ecustomer')
cursor = conn.cursor()

tables_sql = 'show tables'
cursor.execute(tables_sql)
tables = cursor.fetchall()


for t in tables :
    sql = 'select count(*) from  %s'%((t[0]))
    cursor.execute(sql)
    col = cursor.fetchall()
    try:
        c = int(col[0][0])
    except :
        pass 
    print (t[0],c)