"""
Filename: 加密登录.py
Author: 药药
Contact: 1579954422@qq.com
introduce：一个登录系统，注册，可以查看用户数量，有一个存储用户的数据库
"""
# hashlib简单使用
import hashlib
use = []
pas = []

def md5(arg):  # 这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5(bytes('abd', encoding='utf-8'))
    md5_pwd.update(bytes(arg, encoding='utf-8'))
    return md5_pwd.hexdigest()  # 返回加密的数据
use.append('root')
pas.append(md5('123123'))

def log(user, pwd):  # 登陆时候时候的函数，由于md5不能反解，因此登陆的时候用正解
    for i in use:
        if i == user:
            for p in pas:
                if md5(pwd) == p:
                    return True
        else:
            print('用户名不存在')

def register(user, pwd):  # 注册的时候把用户名和加密的密码写进文件，保存起来
    use.append(user)
    pas.append(md5(pwd))
    print('注册成功')
while 1:
    i = input('1表示登陆，2表示注册,3用户数量,4查看数据库:')
    if i == '1':
        user= input('用户名：')
        pwd = input('密码：')
        r = log(user, pwd)  # 验证用户名和密码
        if r == True:
            print('登陆成功')
        else:
            print('密码错误')
    elif i == '2':
        user = input('用户名：')
        if user not in use:
            pwd = input('密码：')
            if len(pwd) >= 3:
                register(user, pwd)         #register(注册模块)
            else:
                print('密码必须大于三位')
        else:
            print('用户名存在')
    elif i == '3':
        print(len(use))
    elif i == '4':
        print(dict(zip(use, pas)))

