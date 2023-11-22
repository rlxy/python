'''
l = ['a'"i q q q ",45,85648,5+4j]       #按道理列表里面啥都能插入
print(l)
'''
'''
#函数append 插入一个内容，在末尾追加
a = [i for i in range(1,5)]
a.append(100)
print(a)
#函数insert：指定插入位置
#函数insert（index，data），插入位置是index前面
print(a)
a.insert(3,99)
print(a)
''''''
s = [1,2,3,4,5,6]
#删除
#del  删除
#pop ，从队尾拿出一个元素，即把最后一个元素取出来放入另一个列表中
print(s)
list = s.pop()
print(list)
print(s)
#remove:在列表中删除指定的值的元素
#删除list指定值的操作应该使用try.....excepty语句，或者先进行判断
print(s)
print(id(s))                    #查看id
s.remove(99)                #把a列表中的99删除，如果删除的是一个没有的值，他就会报错
print(s)
print(id(s))                #输出两个id值一样，宿命remove操作是在原list直接操作
''''''      #clear清空列表
l=[1,2,3,4,5]
print(l)
print(id(l))
l.clear()                    #clear  这是清空的意思
print(l)
print(id(l))                  #清空之后列表还存在。只是列表中的元素没有了
'''