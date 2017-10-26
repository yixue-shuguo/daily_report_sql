# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:28:51 2017

@author: Administrator
"""
#import sys  
#from imp import reload
#reload(sys)  
#sys.setdefaultencoding('utf8')   

import pandas as pd 
from all_common_packages.DB.connect_mysql import mysql
from sql import sql1
host = 'rr-uf647q511648367cso.mysql.rds.aliyuncs.com'
user = 'crm_root'
password = 'Hello2017'
database = 'ecustomer'
charset='utf-8'
conn = mysql(host,user,password ,database,charset)

d1 = pd.read_sql(sql1,conn)
