# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:28:51 2017

@author: Administrator
"""
import pandas as pd 
from all_common_packages.DB.connect_mysql import mysql

host = 'rr-uf647q511648367cso.mysql.rds.aliyuncs.com'
user = 'crm_root'
password = 'Hello2017'
database = 'ecustomer'
conn = mysql(host,user,password ,database)

