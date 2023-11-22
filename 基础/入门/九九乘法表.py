"""
Filename: 01ndarray和图片.py
Author: 药药
Contact: 1579954422@qq.com
introduce：两种九九乘法表写法
"""

def jiujiu():                       # 定义一个函数
    print('九九乘法表')
    for o in range(1, 10):
        for i in range(1, o+1):
            print(o * i, end='  ')         # end：表示每打印一次后面追加一个值，默认是换行的
        print()                             # 这里的print()代表一个回车，每完成一行就一个回车
    return None                         # 这里表示结束这个函数
jiujiu()           # 首先循环第一遍，用1乘1，这一次循环结束，第二遍，用2乘1，2，以此类推，到第九遍用9乘1，9结束循环

def printline(line_num):     # 用def定义一个 printline，参数为linu_num(行号)
    for i in range(1, line_num+1):        # 用range生成的数列赋值给i
        print(line_num * i, end='  ')            # 用linu_num乘一遍i，end是打印完一次行号乘1-行号就追加一个值，这个值是两个空格
    print()                                     # 表示回车，每完成打印一行就打印一次回车
def jiujiu():                              # def定义一个jiujiu函数
    for o in range(1, 10):                       # range生成1-10列数赋值给o
        printline(o)                              # 打印一次12到14行的for循环，并把里面的line_num替换成o
    return None                                  # 结束这个函数