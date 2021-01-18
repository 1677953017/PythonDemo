# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:40:48 2020

@author: Lenovo
"""



#encoding:utf-8                                                                      
import requests                                                                      
from bs4 import BeautifulSoup          
from lxml import etree                                              
import re
import time
urls = ["http://lishi.tianqi.com/wuhan/202004.html",                                 
        "http://lishi.tianqi.com/wuhan/202005.html",                                 
        "http://lishi.tianqi.com/wuhan/202006.html",
        "http://lishi.tianqi.com/beijing/202004.html",
        "http://lishi.tianqi.com/beijing/202005.html",
        "http://lishi.tianqi.com/beijing/202006.html",
        "http://lishi.tianqi.com/shanghai/202004.html",
        "http://lishi.tianqi.com/shanghai/202005.html",
        "http://lishi.tianqi.com/shanghai/202006.html",]                                 
file = open('wuhanbeijingshanghai_weather2.csv','w')       
headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               #'Host':'zhannei.baidu.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}   
for url in urls:                                                                     
    response = requests.post(url,headers=headers)                                                     
    #print(response)
    soup = BeautifulSoup(response.text, 'html.parser')  
    #print(soup)
    weather_list = soup.select('ul[class="thrui"]')  
    #print(weather_list)
    for weather in weather_list:    
        #print(weather)
        for i in range(len(weather.select('li'))):
           # print(str(weather.select('li')[i]))
           # low_tmp=str(weather.select('li')[i].select('div')[1]).replace("</div>","").lstrip('<div style="width: 100px">8</div>')
           # high_tmp=str(weather.select('li')[i].select('div')[2]).replace("<div>","").replace("</div>","")
           # des = str(weather.select('li')[i].select('div')[3]).replace("<div>","").replace("</div>","")
            #print(low_tmp)
            #print(high_tmp)
            #weather_date = weather.select('a')[i]['title']
            #print(weather_date) 
            weather_date=str(weather.select("li")[i].select('div')[0]).replace('<div class="th200">',"").replace("</div>", "")         
            high_tmp=str(weather.select("li")[i].select('div')[1]).replace('<div class="th140">',"").replace("</div>", "")
            low_tmp=str(weather.select("li")[i].select('div')[2]).replace('<div class="th140">',"").replace("</div>", "")
            weather=str(weather.select("li")[i].select('div')[3]).replace('<div class="th140">',"").replace("</div>", "")
            wind=str(weather.select("li")[i].select('div')[4]).replace('<div class="th140">',"").replace("</div>", "")
            print(weather_date)
            print(high_tmp)
            print(low_tmp)
            print(weather)
            print(wind)
            #str1=weather_date+","+low_tmp+","+high_tmp+","+weather
            #print(str1)
           # file.write(str1+'\n')                          
file.close()                                                                         