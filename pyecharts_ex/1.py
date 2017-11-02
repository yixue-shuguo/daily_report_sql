# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:25:35 2017

@author: Administrator
"""

from pyecharts import Gauge

gauge = Gauge("业务指标完成率", title_pos  = 'center')
gauge.add("", "完成率", 67.5)
gauge.show_config()
gauge.render()