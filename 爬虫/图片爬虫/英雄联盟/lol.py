import requests
import urllib.request
n = 0
url = "https://yz.lol.qq.com/v1/zh_cn/search/index.json"

response = requests.get(url)

data = response.json()
print(data['champions'][0]['name'])


for d in data['champions'] :
    name = d['name'] + d['slug']
    for i in range(0,20) :
        n += 1
        a = d['slug'].capitalize()
        url = 'https://yz.lol.qq.com/v1/assets/images/champion/splash/' + a + '_' + str(i) + '.jpg'
        print(url)
        try :
            req = urllib.request.urlopen(url)
            image = req.read()
            with open('./皮肤加默认/{0}.jpg'.format(name+str(n)), 'wb') as f:
                print(name+str(n))
                f.write(image)
        except Exception as e :
            print('文件出错了')
            print(e)
            break


