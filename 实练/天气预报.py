#天气情况数据
#爬虫
#API接口      应用程序接口      API数据接口         聚合科技
#获取 url
from playsound import playsound
import requests
from speech_convert.py import get_speech
item = {
    '温度' : 'temperature',
    '湿度' : 'humidity',
    '天气' : 'info',
    '风向' : 'direct',
    '风力' : 'power',
    '空气质量指数' : 'aqi'
}
app_key = '80a52c2a8c26064c94fc249cf5dfbf37'
url = 'http://apis.juhe.cn/simpleWeather/query'

params = {
    'key':app_key,
    'city':'北京'
}

#response是一个字典  json（）  json数据 =》 字典
response =requests.get(url,params=params) .json()
response_result = response['result']['realtime']

#字符串 =》 音频
output_str = ''
for key,value in item.items():
    output_str += '{}:{},\n'.format(key,response_result[value])

get_speech(output_str)
playsound('audio.mp3')
