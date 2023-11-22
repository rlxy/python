"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：函数文档，函数简单使用
"""

def printline(line_num):
    for i in range(1, line_num+1):
        print(line_num * i, end='  ')
    print()
def jiujiu ():
    for o in range(1,10):
        printline(o)
    return None


# 函数文档
def stu(name,gae, *args):
    '''
    这里写文档的内容
    :param name:   这里对参数进行说明
    :param gae:
    :param args:
    :return: 这里是填返回了什么
    '''
pass
help(stu)            #这里是两种查看方式 使用help函数，形如 help（func）   使用__doc__,
stu.__doc__
