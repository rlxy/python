'''
利用parse模块模拟post请求
分析百度翻译
分析步骤：
1，输入需要翻译的，发现每次输入一个字符都会有请求
2，发现请求地址是  https://fanyi.baidu.com/sug
3.利用NetWork -All - Hearders 找到FormData 的值
3.检查返回内容格式，发现返回的是json 格式内容==>需要用到json包
'''
from urllib import request,parse
#负责处理json格式的模块
import json
'''
大致流程是：
1，利用data构造内容，然后urlopen打开
2，返回一个json格式的结果
3， 结果就应该是翻译的结果
'''
while True :
    baseurl = 'https://fanyi.baidu.com/sug'

    #存放用来模拟form的数据一定是dict格式
    content = input('请输入翻译的内容：')

    data = {
        #girl是翻译输入的内容，应该是由用户输入，此处使用硬编码
        'kw' : content
    }

    #需要使用parse模块对data进行编码
    data = parse.urlencode(data).encode()       #下面data需要的是bytes格式，但是这里不用encode编码的话就是str  encode编码默认utf-8

    #我们需要构造一个请求头，请求头部应该至少包含传入的数据的长度
    #request 要求传入的请求头是一个dict格式

    headers = {
        #因为使用post，至少应该包含content - Length 字段
        'Content-Length':len(data)
    }

    #构造一个Requests的实例
    req = request.Request(url=baseurl,data=data,headers=headers)

    #有了headers ，data，url就可以尝试发出请求了
    # 因为已经构造了一个Requests的请求实例，则所有的请求信息都可以封装在Requests实例中
    rsp = request.urlopen(req)
    json_data = rsp.read().decode()


    #把json_data字符串转化成字典
    json_data = json.loads(json_data)


    for i in json_data['data'] :
        fy = i['k'],'*****',i['v']
        print('翻译结果为：\n{0}'.format(fy))
    if content == '退出' :
        break




