"""
Filename: Series.py
Author: 药药
Contact: 1579954422@qq.com
introduce：数据索引和隐式索引，series介绍和运算
date：2022.9.14
"""
import pandas
import numpy as np
import pandas as pd
from pandas import Series

'''
索引：可以使用中括号取单个索引(此时返回的是元素类型)，或者中括号里一个列表取多个索引（此时返回的仍然是一个Series类型）。
分为显式索引和隐式索引：
（1）显式索引：
    - 使用index中的元素作为索引值
    - 使用.loc[] 
'''
# 注意，此时是闭区间
s = Series(np.random.random(10), index=list('abcdefghij'))
print(s)
# 使用index作索引值
print(s['a'])
print(s[0])
# 显式索引
print(s.loc['a'])

'''
 (2)隐式索引：
    - 使用整数作为索引值
    - 使用.iloc[]
'''
# 注意，此时式半开区间
print(s.iloc[0])

# 切片和上面索引规则一样
# 显式切片
print(s.loc['a':'b'])
print(s['a':'b'])
# 隐式切片
print(s.iloc[0:2])

'''
(3)Series的基本概念
    - 看成一个定长的有序字典
    - 可以通过shape，size，index， values等得到series的属性
'''
# series.values,就是一个ndarray包含关系，是升级的ndarray
print(s.shape, s.size, s.index, s.values)

# 可以通过head(), tail()快速查看Series对象的样式
# df == Dataframe
df = pd.read_csv('data.csv')
print(df)
print(df.head())    # 显示前五个数据
print(df.tail())    # 显示最后五个数据

# 当索引没有对应的值时，可能出现缺失数据显示NaN(not a number)的情况
# 注意:None != np.nan
s = Series([1, 21, None, np.nan], index=list('abcd'))
print(s)
print(type(None), type(np.nan))   # None是NoneType类型，np.nan是float类型

# 可以使用pd.isnull(),pd.notnull(),或自带isnull(),notnull()函数检测缺失数据
# isnull()检测数据是否为空，空的返回True，反则返回False
s2 = s.isnull()
print(s2)
# notnull()检测数据是否不为空，不为空的返回True，反则返回False
s3 = s.notnull()
print(s3)
# 利用这些函数可以过滤一些数据
print('这些数据缺少了\n', s[s2])
print('这些数据是完整的\n', s[s3])

# Series对象本身及其实例都有一个name属性
# name区分，DataFrame中用于区分
s.name = 'not name'
print(s)

# Series运算
# 直接运算,它不会运算Nan的值
s4 = s+10
print(s4)
# Series.add(n, fill_value=None)
# fill_value：在进行运算时，如果，数据中包含Nan，那么fill_value默认将Nan设置为 = 后面的值
s5 = s.add(10, fill_value=0)
print(s5)
# Series设置了索引值再进行相加时，就是索引相同的值相加
s5 = Series([0, 2, 4, 8], index=[0, 1, 2, 3])
s6 = Series([1, 3, 5, 9], index=[2, 3, 4, 5])
print(s5+s6)

