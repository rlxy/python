import requests     #负责爬虫
from lxml import etree       #数据抽取
from time import time
import csv

#城市的名字，城市的拼音，地铁线，地铁站
#爬虫：可见及可爬

#  .html
url = "http://map.amap.com/service/subway?_1566823610521&srhdata=4301_drw_changsha.json"

#1 拿到所有城市数据   城市id，城市拼音，城市名字
response = requests.get("http://map.amap.com/subway/index.html")



# 数据抽取
html = etree.HTML(response.content.decode("utf-8"))            #数据用lxml渲染

morecitylist = html.xpath("//div[@class='city-list fl']/a")
citylist = html.xpath("//div[@class='more-city-list']/a")

citys_a = citylist + morecitylist

citys_info = []
for citys in citys_a:
    id = citys.get("id")        # 城市id
    cityname = citys.get("cityname")        # 城市拼音
    name = citys.text       # 城市名字

    d = {
        'id': id,
        'cityname': cityname,
        'name': name
    }
    citys_info.append(d)

#时间戳  1566823610521

with open('subway.csv', 'w', encoding='utf-8', newline='') as f:
    witer = csv.writer(f)
    witer.writerow("city,cityname,subwayline,subwaystation".split(','))
    for city in citys_info:
        url = f"http://map.amap.com/service/subway?_{round(time()*1000)}&srhdata={city.get('id')}_drw_{city.get('cityname')}.json"
        print(url)
        response = requests.get(url)        #请求数据
        js = response.json()
        # print(js['l'][0]['kn'])
        # print(js['l'][0]['st'][0]['n'])
        # print(js['l'][0]['st'][1]['n'])

        for subline in js['l']:
            sublinename = subline['ln']
            for substation in subline['st']:
                print(substation['n'])
                witer.writerow([city.get('name'),city.get('cityname'),sublinename,substation['n']])


