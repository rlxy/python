"""
Filename: 填数.py
Author: 药药
Contact: 1579954422@qq.com
introduce：一个简单的填数游戏，规定时间内输入指定数字，数位一次次增加
"""
import random
import time
import sys

def ran(a, b):
    Random = random.randint(a, b)
    print('------******leven{}******--------'.format(leven))
    print(f'\033[1;31m{Random}\033[0m')
    print('------********分割线，准备{}秒后输入********---------'.format(t))
    time.sleep(t)
    print('\n\n\n\n\n\n\n\n\n\n')
    print('------********分割线，开始挑战***************---------')
    return Random

def judge(i):
    time1 = time.time()
    a = input('请输入上面出现的数字(单位秒)：')
    if int(a) == i:
        print('恭喜过关，进入下一关')
        print('\033[1;36m本关所花时间：\033[0m', time.time()-time1)
    else:
        print('游戏结束')
        print('有点小差距，再接再厉')
        exit()
def timing():
    return time.time()



if __name__ == '__main__':
    a = 1
    b = 9
    leven = 1
    t = int(input('输入一个需要的时间：'))
    while t >= 10:
        t = int(input('注意！！！选择时间必须小于10：'))
    if judge(ran(a, b)) == 0:
        sys.exit(0)
    while 1:
        a *= 10
        b *= 10
        leven += 1
        time1 = time.time()
        judge(ran(a, b))





