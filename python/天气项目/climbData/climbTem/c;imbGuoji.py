# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 00:21:19 2020

@author: Lenovo
"""
import requests                                                                      
from bs4 import BeautifulSoup          
from lxml import etree                                              
import re
import time

#罗马/纽约州/伦敦/阿姆斯特丹
urls = ['https://www.guowaitianqi.com/h/rome-202003.html',
        'https://www.guowaitianqi.com/h/rome-202004.html',
        'https://www.guowaitianqi.com/h/rome-202005.html',
        'https://www.guowaitianqi.com/h/rome-202006.html',
        'https://www.guowaitianqi.com/h/rome-202007.html',
        'https://www.guowaitianqi.com/h/rome-202008.html',
        'https://www.guowaitianqi.com/h/new-york-202003.html',
        'https://www.guowaitianqi.com/h/new-york-202004.html',
        'https://www.guowaitianqi.com/h/new-york-202005.html',
        'https://www.guowaitianqi.com/h/new-york-202006.html',
        'https://www.guowaitianqi.com/h/new-york-202007.html',
        'https://www.guowaitianqi.com/h/new-york-202008.html',
        'https://www.guowaitianqi.com/h/london-202003.html',
        'https://www.guowaitianqi.com/h/london-202004.html',
        'https://www.guowaitianqi.com/h/london-202005.html',
        'https://www.guowaitianqi.com/h/london-202006.html',
        'https://www.guowaitianqi.com/h/london-202007.html',
        'https://www.guowaitianqi.com/h/london-202008.html',
        'https://www.guowaitianqi.com/h/amsterdam-202003.html',
        'https://www.guowaitianqi.com/h/amsterdam-202004.html',
        'https://www.guowaitianqi.com/h/amsterdam-202005.html',
        'https://www.guowaitianqi.com/h/amsterdam-202006.html'
        'https://www.guowaitianqi.com/h/amsterdam-202007.html',
        'https://www.guowaitianqi.com/h/amsterdam-202008.html'
        ] 
 
file = open('guoji_weather.csv','w')       
headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               #'Host':'zhannei.baidu.com',
              'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Mobile Safari/537.36'} 

for url in urls:                                                                     
    response = requests.get(url,headers=headers)
    #print(response)                                                     
    soup = BeautifulSoup(response.text, 'html.parser') 
    #print(soup)
    weather_list = soup.select('.s-list-wrapper')  
    #print(weather_list)
    
    
    for weather in weather_list:  
        #print(weather)
        weather_data=weather.select('a')
        for i in range(len(weather.select('a'))):
            str1=str(weather_data[i]).replace("]","").replace("&gt;&gt;", "").replace("</a>","").replace(",","").replace("[","").replace("：","，").replace(u'\xa0', u'')
            date = weather.select('a')[i]['title']
            link = 'https://www.guowaitianqi.com/'+weather.select('a')[i]['href']
            #print(link)
            hum_html1=requests.get(link,headers=headers).text
            hum=str(BeautifulSoup(hum_html1,'html.parser').select('.mylocation-detail-state'))[54:65].replace("</","").replace("sp", "").replace("湿度：","")
            #hum=str(hum_html2.select('div')[i].select('span')[1].replace('span',""))
            #print(hum)
            str2=re.sub(r'<.*?>','',str1)
            str3=re.sub('(\d{4})-(\d{2})-(\d{2})，',"",str2)
            #print(str3)
            des0=str3[0:3].replace("，","")
            des=re.sub('(\d{1})',"",des0).replace("特大暴", "特大暴雨")
            temp=str3[2:6].replace("，","").replace("偏","").replace("雨","").replace("西","").replace("北","").replace("东","").replace("南","").replace("℃","")+"℃"
            #print(temp)
            strf=date+","+des+","+temp+","+hum
            print(strf)
            file.write(strf+"\n")                          
file.close() 
    
    
    
    
    
    
     