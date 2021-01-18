# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:24:01 2020
@author: Lenovo
"""


import requests
import jsonpath

#https://report.amap.com/sanjiyisu/roads.do?type=0
res=requests.get("https://report.amap.com/ajax/roadRank.do?roadType=0&timeType=0&cityCode=440100");

print(res.text);