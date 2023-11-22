"""
Filename: pandas的数据结构.py
Author: 药药
Contact: 1579954422@qq.com
introduce：Series类型的创建和介绍以及一个维度报错
date：2022.9.13
"""
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
# 三剑客：pandas, numpy, matplotlib  是处理数据经常用到的三个模块

'''
1.Series
Series是一种类似于一维数组的对象，由两个部分组成：
- values：一组数据(ndarray类型)
- index：相关的数据索引标签
'''

nd = np.array([1, 4, 7, 3, 8, 2])

# 1)Series的创建，两种创建方式：
# -由列表或numpy数组创建，默认索引为0到N-1的整数型索引
s = Series(nd)
print(s)
# 可以通过设置index参数指定索引
s.index = list("abcdef")
print(s)
# 还可以这样
s = Series(nd, index=['张三', '李四', 'Po', 'Michael', 'Lisa', 'Alisa'])
print(s)

# -由字典创建
s2 = Series({'a': 1, 'b': 2, 'c': 4, 'd': 8})
print(s2)

# Data must be 1 dimensional
# Series中存放的数据必须是一维的
# s = Series(np.random.randint(0, 10, size=(5, 2)), index=list('abcde'))
# print(s)    # 报错报错！
# 特别的，由ndarray创建的是引用，而不是副本。对Series元素的改变也会改变原来的ndarray对象中的元素。（列表没有这种情况）
