#列表推导式
a = [i for i in range(100) if not(i % 2) and i % 3]
print(a)


#字典推导式          判断1到10是否为偶数
b = {i:i % 2 ==0 for i in range(11)}
print(b)

#集合推导式       集合里面不会出现相同的数字,并从小到大排列

c = {i for i in [1,5,6,6,3,5,4,2,1,5,2,8,9,9,8,7,7]}
print(c)

#生成器推导式,小括号括起来的是生成器推导式

d = (i for i in range(10))
print(next(d))
print(next(d))
print(next(d))
for i in d:
    print(i)

#这个生成器推导式可以用函数直接推导

e = sum(i for i in range(100) if i % 2 )       #‘sum’为总和，代表把符合条件的数字加起来
            #这里的条件是1 - 100 里面可以整除2的所有的数的总和
print(e)
