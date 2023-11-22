"""
Filename: csv数据读取.py
Author: 药药
Contact: 1579954422@qq.com
introduce：读取文件并介绍pandas
date：2022.9.10
"""
import pandas as pd
'''
python Data Analysis library 或 pandas是基于Numpy的一种工具，
该工具是为了解决数据分析任务而创建的
pandas纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具
pandas提供了大量能使我们快速便捷地处理数据的函数和方法
它使python成为强大而高效的数据分析环境的重要因素之一
'''

# pd读取文件，读取到文件的类型是DataFrame
df = pd.read_csv('data.csv')
print(type(df))

adf = df.values
print(type(adf))    # 读取的来的里面的值是ndarray

