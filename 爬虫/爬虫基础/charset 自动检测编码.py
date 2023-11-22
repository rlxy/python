import urllib.request
import chardet
url = 'https://3w.huanqiu.com/a/a4d1ef/7OY5fTQge2I?agt=8'
rsp = urllib.request.urlopen(url)
html = rsp.read()
cs = chardet.detect(html)       #chardet.detect 检测编码形式
print(cs)
#{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}   cs是个字典形式，检测到的编码在encoding里面，confidence是99的可能是这个编码形式

#保证get取值不会出错
html = html.decode(cs.get('encoding','utf-8'))          #用chardet检测到的编码形式编码  如果没有就按照后面的utf-8解码
print(html)