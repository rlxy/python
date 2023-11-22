"""
Filename: 05ndarray的聚合操作.py
Author: 药药
Contact: 1579954422@qq.com
introduce： 求和（np.sum），最大最小值（np.max/np.min）,其他聚合操作
date：2022.9.9
"""
import numpy as np
import matplotlib.pyplot as plt

th = plt.imread('th.jpg')

# 1.最大值最小值 max/min(axis=None)
n = np.random.randint(0, 100, (4, 4, 4))
print(n)
# axis可以填三个参数，0，1，2，分别是不同的方向的最大值
# 如果没加axis参数，则取所有值中最大值
# 参数为0时，取所有相对应位置的最大值
# 参数为1时，取每列中最大值
# 参数为2时，取每行中最大值
nx = np.max(n, axis=1)
nn = np.min(n, axis=0)
# print(nn)

# 2.平均值,求和，mean/sum()，这里的axis参数在聚合操作中都同理。
nm = np.mean(n, axis=0)
ns = np.sum(n, axis=0)
print(ns)

'''
3.聚合操作集
百分位求值：np.percentile
求方差：np.var
求标准差：np.std
乘积：np.prod
求中位数：np.median
找出最小值的索引：np.argmin
找出最大值的索引：np.argmax
给出条件寻找索引：np.where
验证任何一个元素是否为真：np.any
验证所有元素是否为真：np.all

1. NumPy中的聚合函数往往在python中也有与之相同功能的函数，但是NumPy中的聚合函数能在编译码中进行操作，所以计算得更快一些。
2. 聚合函数的两种用法(以sum为例)：
    ①np.sum(array)
    ②array.sum()
3. 默认情况下，每一个 NumPy 聚合函数将会返回对整个数组的聚合结果。但是可以通过设置axis参数指定沿着哪个轴的方向进行聚合。
4. 大多数的聚合都 有对 NaN 值的安全处理策略（NaN-safe），即计算时忽略所有的缺失值。
'''