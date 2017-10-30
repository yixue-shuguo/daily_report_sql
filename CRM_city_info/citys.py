# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:20:03 2017

@author: Administrator
"""
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select 
from selenium import webdriver
import time
driver=webdriver.Firefox()

url='http://101.132.75.139/Login.php'
driver.get(url)

elem_user = driver.find_element_by_name("user_name")  
elem_user.send_keys("admin")  
elem_pwd = driver.find_element_by_name("user_password")  
elem_pwd.send_keys("yx*crm20170731")  
elem_pwd.send_keys(Keys.RETURN)  
time.sleep(5)  

creat_buttom = driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table/tbody/tr/td[1]')
creat_buttom.click()
time.sleep(5)  

students_buttom = driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table/tbody/tr/td[1]/div/div[1]')
students_buttom.click()





L = []
country = driver.find_element_by_id('bill_country')
state = driver.find_element_by_id('bill_state')
countries = country.text.split('\n')
len_country = len(country.text.split('\n'))

for c in range(len_country):
    Select(driver.find_element_by_id("bill_country")).select_by_index(c)
#    for i in  range(len(driver.find_element_by_id('bill_state').text.split('\n'))):
#        Select(driver.find_element_by_id("bill_state")).select_by_index(i)
    print (countries[c] ,driver.find_element_by_id("bill_state").text.replace('\n',','))
    L.append([countries[c] ,driver.find_element_by_id("bill_state").text])

driver.quit()