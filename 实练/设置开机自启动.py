
import win32api
import win32con
import os,sys


zdynames = os.path.basename(__file__)
name = os.path.splitext(zdynames)[0]
print(zdynames)
print(name)
path = os.path.abspath(os.path.dirname(__file__))+'\\'+zdynames # 要添加的exe完整路径如：
print(path)
# 注册表项名
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
try:
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
    win32api.RegCloseKey(key)
except:
    print('添加失败')
print('添加成功！')
