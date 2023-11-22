
#request.date的使用
    #访问网络的两种方式
        #get    发送数据 优点  1.快
            #利用参数给服务器传递信息
            #参数为dict  然后使用parse编码
        #post   发送数据 优点  1.数据量大 2.安全
            #一般向服务器传递参数使用
            #post是把信息自动加密处理
            #我们如果想使用post信息，需要用到data参数
            #如果使用post，意味着http的请求头部可能需要更改
                #Content-Type ：application/x-www.from-urlencode
                #Content-Length : 数据长度
                #简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
            #urllib.parse.urlencode 可以将字符串自动转化成上面的

#request :  打开和读取urls
#parse  ；解析url的方法
from urllib import request,parse
import chardet

url = 'https://baidu.com/s?'
wd = input('Inout you keyword:')

#想要使用data  需要使用字典结构
qs = {
    'wd' : wd
}
qs = parse.urlencode(qs)
print(qs)
fullurl = url +qs
print(fullurl)

rsp = request.urlopen(fullurl)

html = rsp.read()
cs = chardet.detect(html)
hrml = html = html.decode(cs.get('encoding','utf-8'))

print(html)



