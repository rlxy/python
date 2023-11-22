# -*- encoding:utf-8 -*-
import requests
import json
from urllib.parse import quote


def main():
    context = ""
    jwsession_list = {'9eec3ab867f44aaeb204348c246d6101': "叶俊杰", "6ecddc58ddd0423b87f9900cd221fb11": "黄浩聪",
                      '2d7ce04b4cb94c87ae7b79fbf71bf139': "李新遥"}
    for jwsession in jwsession_list.keys():
        dict = {
            "Accept": "application/json, text/plain, */*",
            "Jwsession": "{}".format(jwsession),
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; ELE-AL00 Build/HUAWEIELE-AL00; wv) AppleWebKit/537.36 ("
                          "KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4343 MMWEBSDK/20221011 Mobile "
                          "Safari/537.36 MMWEBID/9826 MicroMessenger/8.0.30.2260(0x28001E51) WeChat/arm64 Weixin "
                          "NetType/WIFI Language/zh_CN ABI/arm64",
            "Content-Type": "application/json;charset=UTF-8", "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://gw.wozaixiaoyuan.com/h5/mobile/health/index/health/detail?id=7000001",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-us,en",
            "Cookie": "JWSESSION={}; JWSESSION={}".format(jwsession, jwsession)
        }
        try:
            url = "https://gw.wozaixiaoyuan.com/health/mobile/health/save?batch=7000001"
            data = {"location": "中国/江西省/南昌市/南昌县/昌东镇/创新大道/156/360121/156360100/360121109", "type": 0, "locationMode": 0,
                    "locationType": 0}
            dkurl = 'https://sctapi.ftqq.com/SCT184437TqVtrTY2CcWJ7UgTtLqksfqIf.send?title=我在校园每日打卡&desp='
            response = requests.post(url=url, data=json.dumps(data), headers=dict)
            response = json.loads(response.text)
            if response["code"] == 0:
                context += str(jwsession_list[jwsession]) + "打卡成功\n"
            else:
                context += str(jwsession_list[jwsession]) + "打卡失败\n"
        except:
            pass
    dkurl = 'https://sctapi.ftqq.com/SCT184437TqVtrTY2CcWJ7UgTtLqksfqIf.send?title=我在校园每日打卡&desp=' + quote(context)
    requests.get(url=dkurl)


if __name__ == '__main__':
    main()
