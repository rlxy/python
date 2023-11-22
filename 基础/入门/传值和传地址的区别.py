"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：def定义的函数之间传值和传地址
"""

def a(n):            # 这里是传地址
    n[2] = 300       # 给列表第三个数字换成300，这个列表本质上就已经改变       n就是函数a
    print(n)
    return None
def b(n):            # 这里是传值
    n += 100           # 给n变量加上100，n是局部变量，不能影响到全局变量
    print(n)           # 在外面n的全局变量不受影响，函数内的局部变量改变      注意：n是下面函数的传值
    return None
an = [0, 1, 2, 3, 4, 5, 6, 7]
bn = 11

print(an)
a(an)               # 让an列表结合a函数
print(an)           # 这里打印的是和a（an）一样，因为是传地址，直接把第三个数字给替换掉了，这操作影响到这个函数参数

print(bn)
b(bn)
print(bn)           #这里打印出的和上面的b（bn）不一样，因为是传值，所以bn还是bn，和b（bn）是两个不同的数值
