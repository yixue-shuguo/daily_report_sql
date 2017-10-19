# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:19:47 2017

@author: Administrator
"""

import pymysql 
import xlsxwriter

conn = pymysql.connect('rr-uf647q511648367cso.mysql.rds.aliyuncs.com','crm_root','Hello2017','ecustomer')
cursor = conn.cursor()

tables_sql = 'show tables'
cursor.execute(tables_sql)
tables = cursor.fetchall()
workbook = xlsxwriter.Workbook('dic.xlsx') # 建立文件
worksheet = workbook.add_worksheet()


titles = ['表名','字段名','数据类型','不明','key','default','extra']

c = 0 
for title in titles:
    worksheet.write(0,c,title)
    c = c+1


i = 1
for t in tables :
    print (t[0])
    sql = 'desc %s'%((t[0]))
#    print (sql)
    worksheet.write(i,0,t[0])
    cursor.execute(sql)
    d = cursor.fetchall()

    # Iterate over the data and write it out row by row.
    # Start from the first cell. Rows and columns are zero indexed. 按标号写入是从0开始的，按绝对位置'A1'写入是从1开始的

 
    # Iterate over the data and write it out row by row.
    for item1 in d:

        col = 0
        for  item2 in item1 :
            worksheet.write(i, col+1, item2)
            col = col + 1
        i = i+1
workbook.close()