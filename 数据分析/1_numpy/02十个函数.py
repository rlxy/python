"""
Filename: 02十个函数.py
Author: 药药
Contact: 1579954422@qq.com
introduce： 对numpy库内十个函数简单讲解及使用
"""
import numpy as np
import matplotlib.pyplot as plt

'''
2.使用numpy的routines函数创建
包含以下常见创建方法：
    1）np.ones(shape, dtype=None, order="C")
    np.ones()函数返回给定形状和数据类型的新数组，其中元素的值设置为1。此函数与numpy zeros()函数非常相似
'''
n1 = np.ones(shape=(7, 8), dtype=int)
# print(n1)
# 利用图片的格式(长，宽，颜色)创建了一个多维数组，这个数组能够打开变成图片
n2 = np.ones(shape=(100, 100, 3), dtype=float)
# print(n2)
plt.imshow(n2)
# plt.show()

'''
    2) np.zeros(shape, dtype=float, order='C')
    返回来一个给定形状和类型的用0填充的数组
'''
n3 = np.zeros(shape=(4, 4))
# print(n3)

'''
    3) np.full(shape,fill_value,dtype=None,order='C')
    返回一个指定形状、类型和数值的数组
'''
n4 = np.full((5, 5), 1024)
# print(n4)

'''
    4) np.eye(N,M=None,k=0,dtype=float)
    返回的是一个二维2的数组(N,M)，对角线的地方为1，其余的地方为0.
    没有M救默认M=N
    K为对角线的下标，默认为0表示的是主对角线，负数表示的是低对角，正数表示的是高对角
'''
n5 = np.eye(10)
# print(n5)

'''
    5) np.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
    在start和stop之间返回均匀间隔的数据
'''
n6 = np.linspace(0, 20, 9)
# print(n6)

'''
    6)np.arange([start,]stop,[step.]dtype=None)
    返回一个有终点和起点的固定步长的排列，如[1,2,3,4,5]，起点是1，终点是6，步长为1
    start是起点，stop为终点，step为步长， 使用该方法时，数据为左闭右开
'''
n7 = np.arange(0, 50, 10)
# print(n7)

'''
    7)np.random.randint(low,high=None,size=None,dtype='l')
    函数的作用是，返回一个随机整型数，其范围为[low, high)。如果没有写参数high的值，则返回[0,low)的值。
    size参数：输出随机数组的尺寸，比如size = (m, n, k)，则输出数组的shape = (m, n, k)，数组中的每个元素均满足要求。
    size默认为None，仅仅返回满足要求的单一随机数。
    dtype：想要输出的格式。如int64、int等等
'''
n8 = np.random.randint(0, 100, size=(3, 3))
# print(n8)

'''
    8)np.random.randn(d0,d1,...,dn)
    返回一个或一组服从标准正太分布的随机样本值
    标准正太分布是以0为均数，以1为标准差的正太分布，记为N(0,1),
'''
n9 = np.random.randn(100)
# print(n9)

'''
    9)np.random.normal(loc=0.0,scale=1.0,size=None)
    loc(float):正态分布的均值，对应着这个分布的中心。loc=0说明这一个以Y轴为对称轴的正态分布
    scale(float):正态分布的标准差，对应分布的宽度，scale越大，正态分布的曲线越矮胖，scale越小，曲线越高瘦
    size(int 或者整数元组):输出的值赋在shape里，默认为None
'''
n10 = np.random.normal(loc=100, scale=2, size=100)
# print(n10)

'''
    10)np.random.random(size=None)
    生成0到1的随机数，左闭右开
    # 使用随机数生成一张图片
'''
n11 = np.random.random(size=(200, 300, 3))
print(n11)
plt.imshow(n11)
plt.show()
# 这图片没有任何规律
