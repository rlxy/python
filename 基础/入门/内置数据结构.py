"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：列表(list)，元组(tuple)，集合(set)，集合推导式（set comprehension），
字典(dict)各个python内置数据类型的讲解和各种操作，集合序列操作，集合遍历操作，
带有元组的集合遍历，用集合创建集合，集合的各种函数，冰冻集合(frozen set)
"""

'''
#list（列表）
 #一组有顺序的数据的组合
 #创建列表
    #空列表
#创建空列表
l1 = []
#type是内置函数，负责打印出变量的类型
print(type(l1))
#创建带值的列表
l2 = ['hahahah']
print(type(l2))
print(l2)
#创建带多个值的列表
l3 = [1.5,7,8,5,3,6,45,231]
print(type(l3))
print(l3)
'''
'''
#关于元组函数
l = [1,2,3,4,5,6,7,8,9]
print(len(l))   #元组长度
print(max(l))   #元组最大数
print(min(l))   #元组最小数
'''


#set = {1,2,3,4,5}
#dict = {‘1’:a,'2':b....}
'''
#集合set
#集合是一个无序的不重复元素序列
#可以使用大括号{}或set()函数创建jji集合，注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
#创建格式：
# parame = {value01,value02,....}   或者
# set(value)
#实例：
basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)       #去重，把重复的元素去掉
print('orange' in basket)  #判断元素是否在集合内
print('crabgrass' in basket) #不存在，输出False

#两个集合的运算
a = set('abbcccdddd')
b = set('abcefg')
print(a)
print('-:',a-b)  #集合a中包含而集合b中不包含的元素
print('|:',a|b)  #集合a和b中包含的所有元素
print('&:',a&b)  #集合a和b中共同包含的元素
print('^:',a^b)  #不同时包含于a和b中的元素，例如：一个元素存在于b不存在于a，或者存在于a不存在于b

#类似于列表推导式，同样集合支持集合推导式（set comprehension）
c = {x for x in 'abcd' if x not in 'abc'}
print(c)

#集合的基本操作
#添加元素 函数：add
d = set('a b c ')
d.add('d')
print(d)
#还有一个添加元素的方法，且参数可以是列表，元组，字典等 语法:s.update(x)
e = set('a b c ')
e.update({1,2})
e.update([3,4],[5,6])
print(e)

#移除元素 语法格式 s.remove(x)
f = set('gbrt')
f.remove('t')
print(f)
#还有一个方法也是移除集合中的元素，且如果元素不存在不会发生错误
f.discard('a')  #如果‘a'不存在并不会发生错误
#我们也可以设置随机删除集合中的一个元素，语法格式：s.pop()
g = f.pop()
print('被随机删除的元素',g)    #g是被随机删除的元素

#计算集合元素个数 语法：len(s)
h = set('abcd')
print('len计算长度',len(h))
#清空集合 语法：s.clear()
i = set('abcde')
print('clear清空',i.clear())
#判断元素是否在集合中存在 语法格式 x in s
#存在返回true，不存在返回false
j = set('abcd')
print('a' in j)
print('e' in j)
#集合类型
s =set()
print(type(s))
'''


'''
#此时大括号内一定要有值，否则定义出的是一个dict  dict格式：d = {"one":1,"two":2,"three":3}
s = {1,2,3,4,5,6,7}     #这是一个set
print(type(s))

#如果只是大括号定义，则定义的是一个dict类型，空的大括号默认dict类型
d = {}
print(type(d))
print(d)
'''


'''
#集合序列操作
    #成员检测
    #in not in
s = {4,5,'gather','member','operation'}
print(s)
if 'gather' in s :
    print('集合')
if 'xx' not in s :
    print('zy')
''''''
#集合便利操作
#for循环  这里不是按照顺序进行遍历，集合就是一堆无序且不重复的元素
s = {4,5,4,4,4,5,5,5,'gather','member','operation'}
for i in s :
    print(i,end='  ')
''''''
#带有元组的集合遍历
s ={(1,2,3),('i','love','dd'),(4,5,6)}  #留个疑问：如果中间一个元组我只打了2个元素，这个程序就会报错，为什么？
for k,m,n in s :
    print(k,'--',m,'--',n)

for k in s :      #这里直接遍历里面的数组
    print(k)
''''''
#集合的内涵
#以下集合子啊初始化后自动过滤调重复元素
s = {1,63,52,45,11,33,-52,32,-2}
print(s)

#普通集合内涵
#用集合创建集合
ss = {i for i in s }            #用s集合创建一个ss集合
print(ss)
#带条件的集合内涵
sss = {i for i in s if i % 2 ==0}     #如果集合里元素除2余0的话就放到sss集合里面
print(sss)
#带多循环条件的集合内涵
s1 = {1,2,3}
s2 = {'l','x','y'}

s = {m*n for m in s1 for n in s2}
print(s)

s = {m*n for m in s1 for n in s2 if m ==2}
print(s)
''''''
#集合函数/关于集合的函数
#len,max,min;跟其他基本函数一致
s = {25,3,65,45,78,52,13,1,5412}
print(len(s))   #长度  
print(max(s))   #最大值
print(min(s))   #最小值
''''''
#set 生成一个集合
l = [5,3,4,3,5,1,5,3,11]
a = set(l)
print(a)
''''''
#add：向集合内添加元素
a = {1}
a.add(334)
print(a)
''''''
#clear
s = {1,2,3,4,5}
print(id(s))
s.clear()
print(id(s))
#id是同一个，说明clear是原地清空数据

#copy：拷贝
#remove：移除指定的值，直接改变原有的值，如果要删除的值不存在，报错
#discard：移除集合中指定的值，跟remove一样，但是如果要删除的不存在，不报错
s = {3,1,5,95,2}
s.remove(95)
print(s)
s.discard(5)
print(s)
#pop 随机移除一个元素
s = {1,2,3,4,5,6}
d = s.pop()
print(d)            #d是随机移除的那个数字
print(s)            #s是移除数字后的元组
'''
#集合函数
#intersection : 交集
#difference ：差集
#uniom ：并集
#issubset ：检查一个集合是否为另一个子集
#issuperset : 检查一个集合是否为另一个超集
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6}
s3 = s1.intersection(s2)      #s1和s2的交集
print('交集:', s3)
s4 = s1.difference(s2)        #s1和s2的差集
print('差集:', s4)
s5 = s2.issubset(s1)          #s1是否为s2的子集
print('子集:', s5)
s6 = s1.issuperset(s2)        #s1是否为s2的超集
print('超集:', s6)
s7 = s1.union(s2)             #s1和s2的并集
print('并集:', s7)
#frozen set：冰冻集合
#冰冻就是不可以进行任何修改的集合
#frozenset是一种特殊集合
l = {1,2,3,}
s = frozenset(l)
print(type(s))
print(s)
# s.add(123)   #不管对冰冻集合进行任何修改都会报错
