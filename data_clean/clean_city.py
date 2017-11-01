# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:45:19 2017

@author: Administrator
"""

import pandas as pd 


df = pd.read_excel('城市列表.xlsx')
#方法1 
df['城市'].str.split(',', expand=True).stack()

df['城市'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)

city = pd.DataFrame(df['城市'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('city'))



raw  = df.merge(city, left_index =True , right_index =True)


result = raw[['省份','city']]

result.to_excel('city.xlsx')