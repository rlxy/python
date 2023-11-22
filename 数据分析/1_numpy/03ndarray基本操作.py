"""
Filename: 03ndarray基本操作.py
Author: 药药
Contact: 1579954422@qq.com
introduce：ndarray基本操作，索引，切片，变形，利用切片对图片进行颠倒
date：2022.9.7
"""
import numpy as np
import matplotlib.pyplot as plt

# 1.索引  一维与列表完全一致，多维时同理
'''
正索引：0,1,2,3,4,5,6,7,8,9
负索引：-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
值:0,1,2,3,4,5,6,7,8,9
'''
n1 = np.random.randint(0, 100, 10)  # 一维数组
print(n1)
print(n1[3])
n1 = np.random.randint(0, 100, (3, 3))  # 二维数组
print(n1)
print(n1[1][2])
n1 = np.random.randint(0, 100, (3, 3, 3))   # 三维数组
print(n1)
print(n1[2][1][0])
# 根据索引修改数据
n1[2][1][0] = 2
print(n1[2][1][0])

# 2.切片（slice）
'''
Python中符合序列的有序序列都支持切片（slice），例如列表，字符串，元组。
object[start_index : end_index : step]
切片表达式包含两个":" ，用于分隔三个参数（start_index、end_index、step），当只有一个":"时，默认第三个参数step=1。
start_index：表示起始索引（包含该索引本身)；该参数省略时，表示从对象’端点’开始取值，至于是从“起点”还是从“终点”开始，则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。
end_index：表示终止索引（不包含该索引本身）；该参数省略时，表示一直取到数据’端点’，至于是到’起点’还是到’终点’，同样由step参数的正负决定，step为正时直到’终点’，为负时直到’起点’。
step：(步长) , 正负数均可，其绝对值大小决定了切取数据时的“步长”，而正负号决定了“切取方向”，step为正表示“从左往右”取值，step为负表示“从右往左”取值。当step省略时，默认为1，即从左往右以增量1取值。
'''
n2 = np.random.randint(100, size=10)
print(n2)
print(n2[0:5])
# 切片时，数据将会是左闭右开
print('########\n\n')
print(n1[0:1])
print(n1[0:1, 1:3])
print(n1[0:1, 1:3, 0:2])
print(n1[0:1, 1:3, -2:])
# 利用切片符将数据反转，这里可以用于图片的数据反转达到图片进行颠倒
n3 = np.arange(0, 10, 1)
print(n3)
print(n3[::-1])
th = plt.imread('th.jpg')
th1 = (th[::-1])
plt.imshow(th1)
plt.show()

# 变形   使用reshape函数，它的参数是一个tuple
print(n3.shape)
print(n3.reshape((5, 2)))
th = plt.imread('th.jpg')
print(th.shape)
print(th.reshape(245*245*3))    # 对图片数据进行变形，从三维数组变成一维数组ndarray
print(th.reshape(-1))   # 如果是负数，也和上面效果一样
