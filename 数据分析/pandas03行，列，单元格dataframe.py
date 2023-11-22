import pandas as pd

# d = {'x': 100, 'y': 200, 'z': 300}
# series是一个带有名字和索引的一维数组
# s1 = pd.Series(d)   # 用字典创建series
# s1 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])   # 用列表方式创建
# print(s1.index)
# print(s1.values)
# print(s1)

# s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
# s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
# s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
# df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})  # dataframe是一个表格型的数据结构,index的存在利于数据的对齐
# 刚才是用字典讲三个序列加入dataframe 接下来试试用列表加入
# df = pd.DataFrame([s1, s2, s3])   # 和字典相反,这次dataframe把name和index 互换了一下位置,所以使用dataframe时,要注意index的位置
# print(df)

# 之前说index的存在是利于数据的对齐,如果index不同会怎么样
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[2, 3, 4], name='C')  # s3的index没有和其他两个序列对齐
df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
print(df)   # 得到的结果很明显,dataframe把几个索引所缺少的值都定为了NaN,也就是没有数据  s1,s2缺少了 4的index,s3则缺少了 1的index
