"""
Filename: 06ndarray的聚合操作.py
Author: 药药
Contact: 1579954422@qq.com
introduce： 基本矩阵操作(算术运算符-加减乘除)，矩阵积(np.dot)，ndarray的广播机制
date：2022.9.9
"""
import numpy as np

# 加减乘除
n = np.random.randint(0, 10, size=(4, 5))
print(n)
print(n+10)
print(n/2)
# add函数内两个参数相加，两个数组则数组相应位置相加，一个数组一个数字则把数组每个值都加上那个数字
# 和上面的直接运用算术运算符操作类似,加：add,减:subtract,乘:multiply,除:divide
nadd = np.add(n, n)
print(nadd)

# np.dot():返回的是两个数组的点积(dot product)
# 如果处理的是一维数组，则得到的是两数组的内积
# 如果是二维数组(矩阵)之间的运算，则得到矩阵积(mastrix product)
# 所得到的每个元素为：第一个矩阵中的列号与第二个矩阵中的行号相同的元素两两相乘后求和。
n1 = np.random.randint(0, 10, size=(2, 3))
n2 = np.random.randint(0, 10, size=(3, 2))
print(n1, '\n',  n2)
nd = np.dot(n1, n2)
print(nd)

# 广播机制  维度不对应，自动补全
'''
ndarray广播机制的两条规则
1.为缺失的维度补1（这里的1不是自然数，是维度）
2.假定缺失元素用已有值填充
'''
m = np.ones((2, 3))
a = np.arange(3)
print(m, '\n', a, '\n', m+a)

