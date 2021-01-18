# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:55:01 2020

@author: Lenovo
"""
import requests
import jsonpath


city_url="https://report.amap.com/ajax/getCityInfo.do?"
road_url='https://report.amap.com/ajax/roadRank.do?roadType=0&timeType=0&cityCode='

#file = open('map_amap.csv','w')     

headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               #'Host':'zhannei.baidu.com',
              'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Mobile Safari/537.36'} 

#获取城市代号
r=requests.get(url=city_url)
content=r.json()
#print(content)
city_code=jsonpath.jsonpath(content,'$..code')#获取城市编号
#print(city_code)
for code in city_code:
     print(code)
     #city_url0=road_url+str(code)
     #print(city_url0)
     #获取道路情况
     #r2=requests.get(url=city_url0)
     #content2=r2.json()
     #print(content2)
     #道路名称、位置、拥堵指数、速度、旅行时间、延迟时间
     #road_name=jsonpath.jsonpath(content2,'$..name')
     #for road in road_name:
      #    print(road)
























