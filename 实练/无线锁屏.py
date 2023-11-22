#控制windows系统的
import win32com,win32gui,win32api

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

'''
利用死循环去调用windows系统下面的user32.dll动态库
'''
def lock_windows():
    while True:
        user32 = windll.LoadLibrary('user32.dll')
        user32.LockWorkStation()
        time.sleep(5)
lock_windows()

