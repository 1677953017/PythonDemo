# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:44:15 2020

@author: surface
"""

import requests
import datetime
import json


time = datetime.datetime.now().strftime('%Y-%m-%d')
file = open('driveRisk_amap'+"_"+time+'.csv','w') 
file2 = open('overSpeed_amap'+"_"+time+'.csv','w') 
file3 =open('runStatus_amap'+"_"+time+'.csv','w') 

#加表头
file.write("城市编码,城市,高速名称,位置描述,风险值,急刹指数,急转指数,急加指数\n")
file2.write("城市编码,城市,高速名称,位置描述,概率,20%,20%-50%,50%\n")
file3.write("城市编码,城市,高速名称,位置描述,速度差，速度差指数\n")
#驾驶风险路段:主线（0）、桥梁（1）、收费站（2）、出入口（3）
#超速路段（100）、行状态突发路段（do）
urls=['https://report.amap.com/sanjiyisu/roads.do?type=0',
      'https://report.amap.com/sanjiyisu/roads.do?type=1',
      'https://report.amap.com/sanjiyisu/roads.do?type=2',
      'https://report.amap.com/sanjiyisu/roads.do?type=3',
      ]
url0='https://report.amap.com/sanjiyisu/roads.do?type=100'
url1='https://report.amap.com/sanjiyisu/sdRoads.do'
#城市信息
city_url='https://report.amap.com/ajax/getCityInfo.do?'
headers = {
      "cookie": "cna=yjDxFuia4joCAdzIBUqaDjiK; l=eB__t1zPQUg5KJskBO5Nn7ju4gcFZCdfXEVrq4YitIHcC6COpPvMzwRQLCnd-CKRJYXVTuKv4sc4x1vtOecU8yDfagfXmtc4JqODCFYC.; isg=BP39mRaHf4oKONu4m0yQGwWVDFn3mjHsxU_ZqL9H9NQs9joomuszvSPkpWoaw0mk; user_unique_id=a184b07a74ba42fa0174c5eb74dc582c; UM_distinctid=174c5eb98f414-01a2c5ae592f7d-333376b-151800-174c5eb98f541a; SESSION=2096f90e-85e9-4556-95d3-b2eb2ac5f365; CNZZDATA1256662931=2049588335-1601047666-https%253A%252F%252Freport.amap.com%252F%7C1601102593"  
    ,
               #'Host':'zhannei.baidu.com',
              'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Mobile Safari/537.36'} 
#获取城市信息
city_r=requests.get(url=city_url)
city_list=list(json.loads(city_r.text))
def get_city_name(adcode,city_list):
    for  city in city_list:
        if(str(city["code"]) == str(adcode)):
            return city["name"]
    return "null"
           
#获取驾驶风险路段信息
for url in urls:
    r=requests.get(url=url,headers=headers)
    #print(r.text)
    data = json.loads(r.text)
    #print(data)
    #城市,高速名称,位置描述,风险值,急刹指数,急转指数,急加指数
    data=(list)(data)
    for d in data:
        print(d["adcode"],get_city_name(d["adcode"],city_list),d["linkNameChn"],d["addressDesc"],d["ndbkvIndex"],d["brakeIndex"],d["turnIndex"],d["accelerationIndex"])
        #print(tmp)
    for i in range(0,len(data)):
        d = data[i]
        file.write(str(d["adcode"])+","+
                   get_city_name(d["adcode"],city_list)+","+str(d["linkNameChn"])+","+str(d["addressDesc"])+","+
                   str(d["ndbkvIndex"])+","+str(d["brakeIndex"])+","+str(d["turnIndex"])+","+
                   str(d["accelerationIndex"])+"\n")
file.close()

#获取超速路段信息
r0=requests.get(url=url0,headers=headers)
#print(r.text)
data = json.loads(r0.text)
#print(data)
#城市,高速名称,位置描述,概率,20%,20%-50%,50%
data=(list)(data)
for i in range(0,len(data)):
    d=data[i]
    file2.write(str(d["adcode"])+","+
                get_city_name(d["adcode"],city_list)+","+str(d["linkNameChn"])+","+str(d["addressDesc"])+","+
                str(d["speedingPercent"])+","+str(d["speedingLessTwentyPercent"])+","
                +str(d["speedingTwentyFiftyPercent"])+","+str(d["speedingMoreFiftyPercent"])+"\n")
file2.close()

#行状态突发路段
r1=requests.get(url=url1,headers=headers)
#print(r.text)
data= json.loads(r1.text)
#print(data)
#城市,高速名称,位置描述,速度差，速度差指数
data=(list)(data)
for i in range(0,len(data)):
    d=data[i]
    file3.write(str(d["adcode"])+","+
                get_city_name(d["adcode"],city_list)+","+str(d["linkNameChn"])+","+str(d["addressDesc"])+","+
                str(d["avgSpd"])+","+str(d["totSpIndex"])+"\n")
file3.close()