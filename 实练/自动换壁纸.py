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

#括号里面的是形参 里面填的是图片的位置
def desktop_img(bmp_path):
    #打开windows注册表  HKEY_CURRENT_USER 注册表  并且设置属性
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,'Control panel\\Desktop',0,win32con.KEY_SET_VALUE)

    #在HKEY_CURRENT_USER 注册表中写入属性值   WapaperStyle 壁纸风格   0 桌面壁纸居中  2 拉伸桌面
    win32api.RegSetValueEx(k,'WapaperStyle',0,win32con.REG_SZ,'2')      #win32con.REG_SZ  适应桌面
    win32api.RegSetValueEx(k,'TileWallpaper',0,win32con.REG_SZ,'0')

    #刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,bmp_path,win32con.SPIF_SENDWININICHANGE)

desktop_img('F:\\测试文件夹\\桌面文件\\放射.jpg')