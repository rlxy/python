"""
Filename: 08对图片进行操作.py
Author: 药药
Contact: 1579954422@qq.com
introduce：对图片数据进行颠倒达到颠倒图片的效果
date：2022.9.13
"""
import matplotlib.pyplot as plt

th = plt.imread('th.jpg')

# 输出图片
# plt.imshow(th)
# plt.show()

# 图片转换成数据格式是三维数组，[[长]，[高]，[颜色]]
# 在这基础上对图片的长高和颜色进行操作

# 水平颠倒图片
th1 = th[::-1]
plt.imshow(th1)
# plt.show()

# 图片水平方向和垂直方向颠倒
th2 = th[::-1, ::-1]
plt.imshow(th2)
# plt.show()

# 对图片颜色进行颠倒
th3 = th[::, ::, ::-1]
plt.imshow(th3)
# plt.show()

# 似乎达到了马赛克的效果
th4 = th[::5, ::5]
plt.imshow(th4)
# plt.show()

# 别的一些操作
th[::4, ::4] = 0
plt.imshow(th)
plt.show()
