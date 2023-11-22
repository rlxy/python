import pandas
pd = pandas.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
pd = pd.set_index("ID")     # 设置索引，如果没有设置，默认为1，2，3，4
# pd.to_excel("./none.xlsx")  #创建表格
print(pd)
