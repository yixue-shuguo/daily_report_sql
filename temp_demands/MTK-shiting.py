# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:36:08 2017

@author: Administrator
"""
#此处是将 common_packet 加入可引用的目录
import sys
sys.path.append('../')

import pymysql 
import pandas as pd 
from common_packet import get_date,send_mail
yesterday =get_date.getday(1)

conn = pymysql.connect(host = 'rr-uf647q511648367cso.mysql.rds.aliyuncs.com', 
                       user = 'crm_root' ,
                       password = 'Hello2017', 
                       db = 'ecustomer',
                       charset='utf8')

sql = '''
select 
s.shitingsid 试听ID,
s.shitingname 主题,
cl.clueregname 学员姓名,
REPLACE(REPLACE(s.cf_3815, CHAR(10), ''), CHAR(13), '') 意向程度,
s.description 备注,
ac.acctolistname 1对1课程,
s.shiting3061 试听日期,
t.teachername 教师, 
u.last_name 负责人,
u2.last_name 创建人,
s.subject3991 科目,
s.leadsource 招生线索 ,
s_c.c as 试听次数 ,
#s.shiting3071 试听考勤,
#s.clueregsid 数据ID,
#d.createdtime 课前拜访时间,
#d.comments 课前拜访记录,
#c.createdtime 课后回访时间,
REPLACE(REPLACE(c.comments, CHAR(10), ''), CHAR(13), '')  课后回访记录


from ec_shitings s 
left join 
(
#课后跟踪
select a.* from ec_modcomments a,
(
select crmid  , max(createdtime) createdtime 
from ec_modcomments 
where left(comments,4) like '%课后%'
group by crmid 
)b where a.crmid = b.crmid and a.createdtime = b.createdtime 
)c 
on s.shitingsid =c.crmid  
/*
left join 
(
#课前跟踪
select a.* from ec_modcomments a,
(
select crmid  , min(createdtime) createdtime 
from ec_modcomments 
where left(comments,4) like '%课前%'
group by crmid 
)b where a.crmid = b.crmid and a.createdtime = b.createdtime 
)d
on s.shitingsid =d.crmid  
*/
left join ec_clueregs cl 
on s.clueregsid = cl.clueregsid 
left join ec_users u 
on s.smownerid = u.id
left join ec_users u2 
on s.smcreatorid = u2.id
left join ec_acctolists ac 
on s.acctolistsid = ac.acctolistsid
left join ec_teachers t 
on s.teachersid = t.teachersid
left join 
(
select clueregsid,count(*) c
from ec_shitings
group by clueregsid
)s_c  on s.clueregsid = s_c.clueregsid
where DATE_FORMAT(s.shiting3061,'%Y%m%d') =DATE_FORMAT(DATE_SUB(now(),INTERVAL 2 day),'%Y%m%d')
and shiting3071 ='到'
order by s.shiting3061 , s.shiting3071 , s.clueregsid ,c.createdtime 


'''
try:
    d1 = pd.read_sql(sql ,conn)
    file = '昨日试听情况%s.xlsx'%(yesterday)
    writer = pd.ExcelWriter(file)
    d1.to_excel(writer ,'Sheet1',index = False)
    writer.save()
    to_list = ['langzhiyi@171xue.com']
#    to_list = ['mashuguo@171xue.com']
    cc_list = ['mashuguo@171xue.com','guojinyuan@171xue.com']
    sub = '昨天%s试听回访情况，此为自动发送，请知悉。'%(yesterday)
    send_mail.send_mail(to_list ,cc_list  ,sub,file)   
    print ('%s 昨天试听发送成功'%(yesterday))
except Exception as e :
    to_list = ["mashuguo@171xue.com"]
    cc = None
    sub = '今天数据提取发生错误'
    file = None
    print ('%s 昨天试听发送失败')%(yesterday)
