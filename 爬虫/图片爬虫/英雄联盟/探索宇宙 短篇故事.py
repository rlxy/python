import requests
from lxml import etree
from bs4 import BeautifulSoup

url_name = "https://yz.lol.qq.com/v1/zh_cn/search/index.json"

# https://yz.lol.qq.com/v1/zh_cn/champions/syndra/index.json   故事
response = requests.get(url_name)
js = response.json()

list_slug = []
list_name = []
for i in js['champions']:
    list_name.append(i['name'])
    list_slug.append(i['slug'])

for slug in list_slug:
    html = requests.get('https://yz.lol.qq.com/v1/zh_cn/champions/{}/index.json'.format(slug))
    data_story = html.json()
    data = data_story["champion"]["biography"]["full"]
    # print(type(data))
    name = list_name[0]
    del (list_name[1])
    with open("./story/{}.txt".format(name), 'w', encoding='utf-8') as f:
        f.write(data)



print(list_name, '\n', list_slug)





