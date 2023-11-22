import json
import requests

# 登陆接口
# self.loginUrl = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
 
# 登陆
class Login:
    def __init__(self):
        # 账户名或者手机号
        self.username = "13170996631" #手机号
        # 登录密码
        self.password = "123456" #数字密码
 
        # 登陆接口
        self.loginUrl = "https://student.wozaixiaoyuan.com/basicinfo/mobile/login/username"
 
        # 请求头
        self.header = {
            "Host": "student.wozaixiaoyuan.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": "xxxxxxxxxxxxxxx",
            "Content-Length": "29",
        }
 
        # 请求体（必须有） self.body = "{}"
        self.body = "{}"
 
    def login(self):
        
        # 用户名或账号
        url = self.loginUrl + "?username=" + self.username + "&password=" + self.password
        self.session = requests.session()
       
 
        response = self.session.post(url=url, data=self.body, headers=self.header)
        res = json.loads(response.text)
        if res["code"] == 0:
            print("登陆成功")
            # 登录成功获取JWSESSION
            jwsession = response.headers['JWSESSION']
            print(jwsession)
            return True
        else:
            print("登陆失败，请检查账号信息和密码是否正确")
            self.status_code = 4
            return False
 
if __name__ == "__main__":
    Login().login()