
#encoding:utf-8                                                                      
import requests                                                                      
from bs4 import BeautifulSoup          
from lxml import etree                                              
import re
import time
urls = ["http://lishi.tianqi.com/wuhan/202001.html",                                 
        "http://lishi.tianqi.com/wuhan/202002.html",                                 
        "http://lishi.tianqi.com/wuhan/202003.html",
        "http://lishi.tianqi.com/beijing/202001.html",
         "http://lishi.tianqi.com/beijing/202002.html",
          "http://lishi.tianqi.com/beijing/202003.html",
          "http://lishi.tianqi.com/shanghai/202001.html",
         "http://lishi.tianqi.com/shanghai/202002.html",
          "http://lishi.tianqi.com/shanghai/202003.html",]                                 
file = open('wuhanbeijingshanghai_weather.csv','w')       
headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               #'Host':'zhannei.baidu.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}   
for url in urls:                                                                     
    response = requests.post(url,headers=headers)                                                     
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')  
    #print(soup)
    weather_list = soup.select('ul[class="lishitable_content clearfix"]')  
    #weather_list = soup.select('ul[class="thrui"]')  
    #print(weather_list)
    for weather in weather_list:    
        #print(weather)
        for i in range(len(weather.select('a'))):
            #print(str(weather.select('li')[9]))
            low_tmp=str(weather.select('li')[i].select('div')[1]).replace("</div>","").lstrip('<div style="width: 100px">8</div>')
            high_tmp=str(weather.select('li')[i].select('div')[2]).replace("<div>","").replace("</div>","")
            des = str(weather.select('li')[i].select('div')[3]).replace("<div>","").replace("</div>","")
            #print(low_tmp)
            #print(high_tmp)
            weather_date = weather.select('a')[i]['title']
            #print(weather_date)             
            str1=str(weather_date)+","+low_tmp+","+high_tmp+","+des
            print(str1)
            file.write(str1+'\n')                          
file.close()                                                                         