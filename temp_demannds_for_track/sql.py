# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:48:51 2017

@author: Administrator
"""

sql1 = '''



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
where DATE_FORMAT(s.shiting3061,'%Y%m%d') between DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 4 DAY),'%Y%m%d')and DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 2 DAY),'%Y%m%d')
order by s.shiting3061 , s.shiting3071 , s.clueregsid ,c.createdtime 

'''
