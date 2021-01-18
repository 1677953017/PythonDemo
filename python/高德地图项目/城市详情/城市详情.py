# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:09:51 2020

@author: surface
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:05:30 2020

@author: surface
"""
import time
import datetime
import requests
import jsonpath
import json

city_url="https://report.amap.com/ajax/getCityInfo.do?"
road_url='https://report.amap.com/ajax/roadRank.do?roadType=0&timeType=0&cityCode='

#file = open('map_amap.csv','w')      

headers = {'Accept': 'textcml, application/xhtml+xml, image¬r, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               #'Host':'zhannei.baidu.com',
              'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Mobile Safari/537.36'} 

#获取城市代号
r=requests.get(url=city_url)
city_list=list(json.loads(r.text))
#print(content)

 
#print(city_code)
for city in city_list:
     code = city["code"]
     name = city["name"]
     #print(code)
     city_url0=road_url+str(code)
     #print(city_url0)
     #获取道路情况
     i=0
     while(i<10):
         try:
             r2=requests.get(url=city_url0)
             content2 = json.loads(r2.text)
     #print(content2)
     #道路名称、位置、拥堵指数、速度、旅行时间、延迟时间
             road_name=(list)(jsonpath.jsonpath(content2,'$..name'))
             i=0
             break
         except:
             print("retry",str(i))
             i=i+1
             time.sleep(30)
             continue
     
     #print(road_name)
     tmp=[]
     for road in road_name:
         tmp.append(road)
     road_location=(list)(jsonpath.jsonpath(content2,'$..dir'))
     for r in road_location:
         tmp.append(r)
     road_index= list( jsonpath.jsonpath(content2,'$..index'))
     road_speed= list( jsonpath.jsonpath(content2,'$..speed'))
     road_traveltime= list( jsonpath.jsonpath(content2,'$..travelTime'))
     road_time= list( jsonpath.jsonpath(content2,'$..delayTime'))
     print(tmp)
     
     time = datetime.datetime.now().strftime('%Y-%m-%d')
     
     file2 = open(str(city["name"])+"_"+time+ '.txt', 'w')
     for i in range(0,len(road_name)):
         file2.write(str(code)+","+name+","+str(road_name[i])+","+str( road_index[i])+","+str(road_speed[i])+","+str(road_traveltime[i])+","+str(road_time[i])+"\n")
     file2.close()
     
     
