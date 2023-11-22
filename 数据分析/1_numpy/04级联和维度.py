"""
Filename: 04级联和维度.py
Author: 药药
Contact: 1579954422@qq.com
introduce： 级联，水平级联与垂直级联，concatenate函数可以对数组进行级联，并变更级联方向，可以用作拼接图片，
np.hstack与np.vstack可以进行维度的变更，切分：split，行切分：vsplit，列切分：hsplit，ndarray类型副本说明
date：2022.9.7
"""
import numpy as np
import matplotlib.pyplot as plt

'''
级联  np.concatenate()级联需要注意的点：
1.级联的参数是列表：一定要加中括号或小括号
2.维度必须相同
3.形状相符
4.【重点】级联的方向默认是shape这个tuple的第一个值所代表的维度方向
5.可通过axis参数改变级联的方向
'''
n1 = np.random.randint(1, 10, size=(5, 5))
print(n1)
n2 = np.concatenate([n1, n1])
print(n2)
n2 = np.concatenate([n1, n1], axis=1)
print(n2)
# 利用concatenate来对图片进行级联操作
th = plt.imread('th.jpg')
# plt.imshow(th)
# plt.show()
ths = np.concatenate([th, th], axis=1)  # 把两张图片的数据级联在一起，这两张图片就会变成一张【axis可以改变级联的方向】
plt.imshow(ths)
# plt.show()

# np.hstack与np.vstack   水平级联与垂直级联，进行维度的变更
n3 = np.random.randint(1, 10, size=(5, 5))
print(n3)
n3 = np.hstack(n3)
print(n3)

n3 = np.vstack(n3)
print(n3)
n4 = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8]])
print(n4)
n4 = np.hstack(n4)
print(n4)
nth = np.hstack(th)     # 将图片的维度进行变更
print(nth, '\n')              # 这里已经是二维了
nth = np.hstack(nth)    # 再套一层就变成一维了
print(nth)

'''
切分
与级联类似，三个函数完成切分工作：
np.split：切分
np.vsplit：行切分
np.hsplit：列切分
'''
n5 = np.random.randint(1, 100, size=(5, 7))
print(n5)
# split的axis参数默认为0表示按行切，设定为1时，则按列切
n6 = np.split(n5, (1, 3))
print(n6)
# 利用split函数对图片进行切分
print(th.shape)
# 把图片切成了三份
th2 = np.split(th, (100, 100))[2]
plt.imshow(th2)
# plt.show()

# vsplit:切分行
n7 = np.vsplit(n5, (1, 3))
print(n7)
# hsplit:切分列
n8 = np.hsplit(n5, (1, 3))
print(n8)

'''
副本  所有赋值运算不会为ndarray的任何元素创建副本。对赋值后的对象的操作也对原来的对象生效

'''
ls = [1, 2, 3, 4]
n = np.array(ls)
# ls 是list类型，n是ndarray
print(ls)
print(n)
n[2] = 999
print(ls)
print(n)
# 这里的操作对两个变量没有影响，接下来换成两个ndarray类型变量
n10 = n
n10[2] = 1024
print(n10, n)
# 可以看出n10内的数据改变让n内的数据同步变化，他们两个变量指向的是同一个ndarray，没有额外的副本
# 不过对于这个，我们可以用copy函数创建副本
n11 = n.copy()
n11[0] = 1024
print(n10, n, n11)
# copy出来的副本进行操作不会影响原来的ndarray

