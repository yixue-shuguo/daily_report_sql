# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:36:08 2017

@author: Administrator
"""
#此处是将 common_packet 加入可引用的目录
#import os
#dirs = os.path.join( os.path.dirname(__file__),'../')  #上上级文件目录名
#os.sys.path.append(os.path.join( os.path.dirname(__file__), '../'))   #将上上级目录加载到python的环境变量中。
#
#
import sys
sys.path.append('../..')

#import os
#import sys
#parent_dir_name =os.path.dirname(os.path.realpath(__name__))
#sys.path.append(parent_dir_name + os.sep+'common_packet'+ os.sep)
#

import pymysql 
import pandas as pd 
from common_packet import get_date,send_mail
today =get_date.getday(0)
last_2_days = get_date.getday(2)
last_4_days = get_date.getday(4)


print('%s 包引入成功'%(today))
conn = pymysql.connect(host = 'rr-uf647q511648367cso.mysql.rds.aliyuncs.com', 
                       user = 'crm_root' ,
                       password = 'Hello2017', 
                       db = 'ecustomer',
                       charset='utf8')

print('%s 数据库成功连接'%(today))

sql = '''

select 
s.shitingsid 试听ID,
s.shitingname 试听编码,
cl.clueregname 学员姓名,
u.last_name 负责人,
s.shiting3071 试听考勤,
concat(s.shiting3061 ,' ', right(s.shiting3063,5),':00') 试听日期,
s.clueregsid 数据ID,
d.createdtime 课前最早拜访时间,
d.comments 课前最早拜访记录,
d.createmax 课前最晚拜访时间,
d.before_c 课前拜访次数,
c.createdtime 课后最早回访时间,
c.comments 课后最早回访记录,
c.createmax 课后最晚回访时间,
c.after_c 课后回访次数 ,
TIMESTAMPDIFF(HOUR, d.createmax ,concat(s.shiting3061 ,' ', right(s.shiting3063,5),':00')) 试听距最后拜访小时数, 
TIMESTAMPDIFF(HOUR  ,concat(s.shiting3061 ,' ', right(s.shiting3063,5),':00'),c.createdtime) 试听距最早回访小时数
from ec_shitings s 
left join 
(
#课后跟踪
select a.*,b.createmax, b.after_c from ec_modcomments a,
(
select crmid  , min(createdtime) createdtime ,max(createdtime) createmax ,count(*) after_c
from ec_modcomments 
where left(comments,4) like '%课后%'
group by crmid 
)b where a.crmid = b.crmid and a.createdtime = b.createdtime 


)c 
on s.shitingsid =c.crmid  
left join 
(


#课前跟踪
select a.*,b.createmax,b.before_c from ec_modcomments a,
(
select crmid  , min(createdtime) createdtime ,max(createdtime) createmax, count(*) before_c
from ec_modcomments 
where left(comments,4) like '%课前%'
group by crmid 
)b where a.crmid = b.crmid and a.createdtime = b.createdtime 


)d
on s.shitingsid =d.crmid  
left join ec_clueregs cl 
on s.clueregsid = cl.clueregsid 
left join ec_users u 
on s.smownerid = u.id
where DATE_FORMAT(s.shiting3061,'%Y%m%d') between DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 4 DAY),'%Y%m%d')and DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 1 DAY),'%Y%m%d')
order by s.shiting3061 , s.shiting3071 , s.clueregsid ,c.createdtime 

'''
try:
    d1 = pd.read_sql(sql ,conn)
    file = '%s到%s试听跟进情况.xlsx'%(last_2_days,last_4_days)
    writer = pd.ExcelWriter(file)
    d1.to_excel(writer ,'Sheet1',index = False)
    writer.save()
    to_list = ['guojinyuan@171xue.com']
#    to_list = ['mashuguo@171xue.com']
    cc_list = ['mashuguo@171xue.com']
    sub = '%s到%s试听课的课前课后具体信息，此为自动发送，请知悉。'%(last_2_days,last_4_days)
    send_mail.send_mail(to_list ,cc_list  ,sub,file)   
    print ('%s 今天试听发反馈送成功'%(today))
except Exception as e :
    to_list = ["mashuguo@171xue.com"]
    cc = None
    sub = '今天数据提取发生错误'
    file = None
    print ('%s 今天试听发反馈送失败')%(today)
