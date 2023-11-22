"""
Filename: 07_ndarray的排序.py
Author: 药药
Contact: 1579954422@qq.com
introduce：利用for循环简单排序，快速排序，部分排序
date：2022.9.11
"""
import numpy as np

n1 = np.array([3, 2, 6, 1, 9])
# 简单的排序，利用两层循环排序
def simple_sort(nd):
    """
    用双层for循环对一个ndarray进行排序
    """
    for i in range(nd.size):
        for j in range(i, nd.size):
            if nd[i] > nd[j]:
                nd[i], nd[j] = nd[j], nd[i]
    return nd
# print(simple_sort(n1))
# 降低运算的空间复杂度和时间复杂度
def sort(nd):
    """
    优化一下，在函数中利用np.argmin，达到减少一层循环的目的
    """
    for i in range(nd.size):
        # 由于使用了冒号进行切片，导致索引不对应
        index_min = np.argmin(nd[i:]) + i
        nd[i], nd[index_min] = nd[index_min], nd[i]
    return nd
print(sort(n1))

# 快速排序
print('快速排序')
'''
np.sort()与ndarray.sort()都可以，区别在于：
- np.short()不改变输入
- ndarray.sort()本地处理，不占用空间，但改变输入
'''
n1 = np.random.randint(0, 100, size=10)
print(n1)
# ndarray.sort(),直接改变了n1的值
n1.sort()
print(n1)
# np.sort(),这个函数带一个return，不会改变原来的值
n2 = np.random.randint(0, 100, size=10)
print(n2)
n2 = np.sort(n2)
print(n2)

# 部分排序
print('部分排序')
'''
np.partition(a,k)
有时候需要的不是全部的数据，而是只针对最小或最大的一部份值
- 当k为正时，我们想要得到最小的k个数
- 当k为负时，我们想要得到最大的k个数
【得到的值并不是按从大到小或从小到大排序的，只是为你得到】
'''
n3 = np.random.randint(0, 100, size=10)
print(n3)
n3 = np.partition(n3, 5)
print(n3[:5])
