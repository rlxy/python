import pandas as pd

response = pd.read_excel("./data2.xlsx", index_col='ID')
# response.sort_values(by='班级总人数', inplace=True, ascending=False)  # inplace表示再当前的dataframe上操作,ascending默认为升序
# response.sort_values(by=["排名", "班级总人数"], inplace=True)    # 同时对两列数据先后进行排序
response.sort_values(by=["学习人数", "班级总人数"], inplace=True, ascending=[False, True])   # 对两列数据进行不同的顺序排序


print(response)

