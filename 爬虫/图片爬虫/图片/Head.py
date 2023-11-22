import requests
from  bs4 import BeautifulSoup
b = 0
for a in range(2,22) :
    url = 'https://m.woyaogexing.com/touxiang/z/ydlz/index_{0}.html'.format(a)
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')       #图片需要用content
    print(soup)
    img_list =soup.find_all('a',attrs={'href':True},target="_blank")  #获取a标签中的href里面的超链接

    for img in img_list :
        ur = img.get('href')
        l = 'https://m.woyaogexing.com'
        url = l + ur
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'lxml')
        soup = soup.find_all('div',class_='swipebox-img box square')
        for i in soup :
            image_list = i.find_all('img', class_='lazy', attrs={'data-src': True})
            for l in image_list:
                b +=1
                l = l.get("data-src")
                l = l.replace("jpeg",'webp')
                ur = 'http:'
                url = ur + l
                print(url)
                with open('./{}.webp'.format(b),'wb') as f :
                    img = requests.get(url).content
                    f.write(img)
