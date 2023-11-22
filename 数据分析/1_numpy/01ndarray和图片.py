"""
Filename: 01ndarray和图片.py
Author: 药药
Contact: 1579954422@qq.com
introduce： 对图片底层数据和numpy.array()简单说明，使用matplotlib.pyplot函数对图片数据简单操作，ndarray元素类型说明
"""
import numpy as np
import matplotlib.pyplot as plt  # pyplot 显示画图，数据分析与可视化

# print(np.__version__)

th = plt.imread('th.jpg')  # 读取图片
# print(th)
# 图片是由N维数组组成的，[R,G,B] 对应 [253 253 253]
# print(type(th))
# th2 = th - 5
# plt.imshow(th)
# plt.show()


''' 
1.使用np.array()由python list创建,参数为列表:[1,4,5,8,3]
'''
# n1 = np.array([1, 4, 5, 8, 3])
# print(n1)
# print(n1.shape)     # shape是形状，这里是对n1这个list形状的说明  （行，列）
# n2 = np.array([[2, 4, 5, 23], [3, 4, 5, 6], [7, 8, 9, 0]])
# print(n2)
# print(n2.shape)

# 任何一张2维的图片转换成数据是三维数组，长，高，颜色
# print(th.shape)

'''
注意：
    numpy默认ndarray的所有元素的类型是相同的
    如果传进来的列表中包含不同的类型，则统一为同一类型，优先级为：str>float>int
'''
n3 = np.array(list('ABED'))
print(n3)
n4 = np.array([1, 3.14, 'gogo'])
print(n4)
