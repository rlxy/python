import urllib.request
import urllib.parse         #url解析组件
import json                 #json是文本数据交换格式
while 1:
    yd = input('在线翻译：')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = yd
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15648890154563'
    data['sign'] = 'bd4fa9f521a4ef3a08b4045e3eae4477'
    data['ts'] = '1564889015456'
    data['bv'] = '1799e7e181945d3004c70788458c9d92'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode('utf-8')       #用urlencode解析data，并且用encode把解析出来的格式转换成utf-8

                                    #encode的作用是将unicode编码转换成其他编码的字符串
    response = urllib.request.urlopen(url, data)            #request传入urlopen打开的url，data给response

    html = response.read().decode('utf-8')                  #用read读出response的是utf-8的文件，所以后面要用decode把其他编码形式编程utf-8
                        #decode的作用是将其他编码的字符串转换成unicode编码
    target = json.loads(html)       #用loads将已编码的json字符串解码为python的对象

    print('译文：%s' % (target['translateResult'][0][0]['tgt']))
                    #json.loads解码出来的是一个字典,字典下面是列表列表字典

    continue





'''
json函数
json.dumps	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象

python data = json.loads(需要解码的json的data)
json data = json.dumps（需要解码的python的data）
上面的html是read读出来的数据，这个数据是json对象，下面就用了json.loads这个函数来解码成python对象

'''

'''
encode和decode
字符串在python内部是unicode编码
上面用urlencode解析data的文件需要用encode来转换成utf-8的形式
下面的decode是将read读出来的response文件解码成unicode
decode()：是解码
encode()：是编码
'''
