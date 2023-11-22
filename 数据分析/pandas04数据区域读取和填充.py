import pandas as pd
from datetime import date, timedelta

# 如果数据中存在大量空行该怎么读取,这里可以用到两个属性
response = pd.read_excel('./none.xlsx', skiprows=4, usecols='B:E', dtype={'index': str})
# skiprow:跳过几行  usecols:使用几列,也可以手动输入列,冒号连接为C到D


# 修改单元格内的值,修改index那一列的值
# data['index'].at[0] = '1'  # 这里修改了index下第一行的值,如此想要修改这一列所有的值使用一个循环就可以做到了
for i in response.index:
    response['index'].at[i] = i+1
# 为什么这里所添加的数字是float类型,我们想要的是int怎么办
# 在read_excel 加上dtype属性指定某一列的类型就好了,不过注意这里不能修改成int类型,所以修改成str类型,这样也是把小数点去掉的


def add_month(d, md):
    yd = md // 12           # 如果md整除12 就代表多一年
    m = d.month + md % 12   # 因为12月是一年,余12进了1,剩几月进几月
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


# 在空单元格内填充日期
start = date(2018, 1, 1)

for i in response.index:
    # 下面是拿到response.date的series的值修改,,还可以直接修改值
    # response['date'].at[i] = start + timedelta(days=i)      # timedelta 仅仅只可以用来修改day以下的时间,修改不了month和year
    # 如果要添加month和year我们可以这样,不过对于month的增加有点麻烦,因为需要逢12个月进一年,需要一个小算法,小算法在上面
    # response['date'].at[i] = add_month(start, i)
    # 我们试试直接修改单元格的值
    response.at[i, 'date'] = add_month(start, i)

response.set_index('index',inplace=True)
# response.to_excel('./none.xlsx')
print(response)




