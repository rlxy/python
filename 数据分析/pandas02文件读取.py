import pandas as pd

# data = pd.read_excel('data.xlsx')            #读取文件
# print(data.shape)        # shape 用来统计数据的 行，列
# print("---------")
# print(data.columns)      # 打印表格的列
# print("---------")
# print(data.head(3))      # 从开头开始打印表格数据，默认5行
# print("---------")
# print(data.tail(3))      # 从结尾开始打印表格数据，默认5行

# data = pd.read_excel('data.xlsx',header=1)    # header=1 从第一行开始读取
# data = pd.read_excel('data.xlsx',header=None)  #None 为不要设置任何header
# data.columns = ['ID', '下属组织名称', '班级总人数', '学习人数', '排名', '辅导员']  # 自定义列
# # data = data.set_index('ID')        # 修改索引开始位置,不设置索引表格会自动生成一行索引
# data.set_index('ID', inplace=True)  # 和上句一个作用


data = pd.read_excel('data2.xlsx', index_col='ID')   #直接指定索引开始读取
print(data.head())








