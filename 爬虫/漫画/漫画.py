import requests    #爬虫
from lxml import etree
from PIL import Image           #image  是 基本的图像处理操作
from io import BytesIO          #需要二进制操作，实现在内存中读写bytes


#获取源代码
root = 'https://www.manhuatai.com/nietuzaishang/'
response=requests.get(root)

#数据抽取
html = etree.HTML(response.text)    #能够抽取的
lis = html.xpath("//ol[@id='j_chapter_list']/li/a/div/img/@data-src")  #数据抽取的页面标签

count = 0   #控制第几话
imgs = []  #存放着所有图片
for li in lis:
    li = li.replace('cnmanhua','manhualang')            #replace  把旧的字符串替换成新的 str.replace(old, new[, max])
    li = li.strip(".jpg-300x1502")                      #strip  用于删除开头或者结尾指定字符，不能删中间的

    index = 1
    while True:
        #这里是提每话里面每张图片的url
        url = f'https:{li}{index}.jpg-mht.middle.webp'       # f前缀表示在字符串内支持大括号内的python 表达式
        print(url)
        index += 1
        resp = requests.get(url)

        #response.text 与 response.content 都是来获取response中的数据信息
        #response.text返回的是一个unicode型的文本数据
        #response.content返回的是bytes型的二进制数据
                                     #  b" "前缀表示：后面字符串是bytes 类型。
        if resp.content.startswith(b'<?xml'):       #startswith函数用于匹配字符串开头和结尾是否包含一个字符串，返回布尔类型
            break

        im = Image.open(BytesIO(resp.content))      #用image图片处理   BytesIO实现了在内存中读写bytes格式，content返回的是bytes型的二进制数据

        imgs.append(im)
    if count > 10:
        break

imgs[0].save("小说名.pdf",save_all = True,append_images = imgs[1:])












    
    
    
    
    
    
    
    
    
    
    
    
