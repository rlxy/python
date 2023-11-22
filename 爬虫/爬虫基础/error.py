#urllib.error
    #URLError产生的原因：
        #没网
        #服务器链接失败
        #找不到指定务器
        #URLError是 OSError的子类
    #HTTPError，是URLError的子类

    #两种错误的区别：
        #HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上，则引发HTTPError
        #URLError对应的一般实网络出现问题  包括url问题
        #关系区别 ： OSError-URLError-HTTPError

#URLError的使用
from urllib import request,error


url = 'http://www.baidu.com'
try:
    req = request.Request(url)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
except error.HTTPError as e :
    print('HTTPError:{0}'.format(e.reason))
    print('HTTPError:{0}'.format(e))
except error.URLError as e :
    print('URLError{0}'.format(e.reason))
    print('URLError:{0}'.format(e))
except Exception as e :
    print(e)