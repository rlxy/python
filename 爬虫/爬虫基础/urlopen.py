#urlopen 的返回对象
    #geturl ： 返回请求对象的url
    #info ：请求反馈对象的meta信息
    #getcode ： 返回http code
import urllib.request
import chardet
url = 'https://3w.huanqiu.com/a/a4d1ef/7OY5fTQge2I?agt=8'
rsp = urllib.request.urlopen(url)

print(type(rsp))            #可以打个断点在这里然后右击运行 Debug'urlopen'   里面也会显示出需要的数据
print(rsp)
# print('URL : {0}'.format(rsp.geturl()))
# print('Info :{0}'.format(rsp.info()))
# print('Code:{0}'.format(rsp.getcode()))



# html = rsp.read()
# cs = chardet.detect(html)
# print(cs)
# html = html.decode(cs.get('encoding','utf-8'))
# print(html)