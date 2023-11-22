"""
爬取油管视频,使用requests.get不知道为什么会报错
date:2022.13.31
正则用不出来 继续不下去了
"""
import re
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=MohF1P6rZDQ&list=PLUJleL1PBOirG-RD46v98eIXLpE2IGnz1'
headers = {
    'cookie': 'SID=QAigVmqddeebg00edh8pFP16ix1JTtCOW3sGpm5gre5TRCFEvIx_qSdI7tvXjb6LBhBt5A.; APISID=99GX_lapLrglmAve/AcAoIaoDnn4ZSgv_K; SAPISID=X8kcA8csCHtja8YD/AMWVyhXILR8yX24Cf; __Secure-1PAPISID=X8kcA8csCHtja8YD/AMWVyhXILR8yX24Cf; __Secure-3PAPISID=X8kcA8csCHtja8YD/AMWVyhXILR8yX24Cf; SIDCC=AIKkIs3u6-nEzNIfOlTMYV4m3ZwNTFVM6XgDCm_J7RiBxt6Eyyfv0rdNIpOiaNnCW-f0eYBSmZE; PREF=f4=4000000&tz=Asia.Shanghai&f6=40000000&f5=30000',
    'Referer': 'https://www.youtube.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}

HTML = urllib.request.urlopen(url).read()
response = BeautifulSoup(HTML.decode("utf-8"), 'lxml')

reg = '/<"watchEndpoint":(.)+params/>'

response = response.find_all(text=re.compile(reg))


#
# "watchEndpoint":{"videoId":"[a-zA-Z0-9_]","playlistId":"[a-zA-Z0-9_]","index":([0-9])
# "watchEndpoint":{"videoId":"MohF1P6rZDQ","playlistId":"PLUJleL1PBOirG-RD46v98eIXLpE2IGnz1","index":0
# 'https://www.youtube.com/watch?v=MohF1P6rZDQ&list=PLUJleL1PBOirG-RD46v98eIXLpE2IGnz1&index=1'
# 'https://www.youtube.com/watch?v=gxd_x3-K-mE&list=PLUJleL1PBOirG-RD46v98eIXLpE2IGnz1&index=2'
# 'https://www.youtube.com/watch?v=DzLNnWlNGR0&list=PLUJleL1PBOirG-RD46v98eIXLpE2IGnz1&index=4'
# 'https://www.youtube.com/watch?v=hJLL4-ASncI&list=PLUJleL1PBOirG-RD46v98eIXLpE2IGnz1&index=19'
# 'watchEndpoint'
print(response)
