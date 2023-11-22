"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：列表的基本操作，列表的循环，其他格式转换成list
"""

#list   列表
#列表的访问
a = [2,4,3,1,5,6,7]    #列表里面的数字下标从0开始，为 0，1，2，3，4
c = [1,2,5,3,]
print(type(a))          #type是内置函数，负责打印出变量的类型    这里的类型是列表(list)
print(a)
#访问列表     分片处理     分片操作是生成一个新的列表，并不是在原来的列表操作
print(a[0:5])         #这里打印的是 a 列表里面第0到4个数字，，访问，左包括，右不包括
print(a[0:])          #这里打印的是从0到最后一个数字，右边为空则默认最后一位
print(a[:5])          #左边为空，左边默认为第0位
print(a[0:8:2])       #打印从0到7的数字，每次打印增长的幅度为2（每次打印前一次打印的后面第二位数字）
del a[1]              #删除a列表第2位数
b = a + c             #a列表加上c 列表 生成b列表
v = a * 2             #a列表乘2遍生成v列表

#成员资格运算
#判断一个元素是否在list里面
a = [1,2,3,4,5,6]
b = 7
c = b in a     #b的值不在a里，所以c是假的值，false
print(c)
b = 4
c = b in a     #b的值在a 中所以c是真的值true
print(c)
#not in
a = [1,2,3,4,5,6]
b = 10
print(b not in a)         #b没在a里面，所以为真

#链表的遍历   for  while
#for in list
a = [1,2,3,4,5]
#挨个打印列表里面的元素
for i in a :
    print(i)
#while循环访问list
#一般不哦那个while便利list
a = [1,2,3,4,5,6]
length = len(a)
indx = 0                            #indx表示list的下标
while indx < length :                        #这个用while遍历的太麻烦，所以一般不使用
    print(a[indx])
    indx += 1

#双层列表循环
#a为嵌套列表，或者叫双层列表
a = [['one',1],['two',2],['three',3]]
for k,v in a:                    #a里面的两个值分别赋值给k和v
    print(k,'--',v)                     #k，v的个数应该跟解包出来的变量个数一致

#列表函数
#通过简单方法创作列表
#for创建
a = [1,2,3,4,5,6]
#用list a创建一个list b
#a里面的列表命名为i，然后所有元素逐个放入新的列表b中
b = [i*10 for i in a]     #这里的*10是，乘i列表里面的元素然后重新放入列表
print(b)

#还可以过滤原来list中的内容并放入新列表
#比如原有列表a，需要把a中所有的偶数生成新的列表
a = [x for x in range(1,21)]        #生成1到20的一个列表
b = [m for m in a if m % 2 == 0]
print(b)

#列表生成可以嵌套
#由两个列表a,b
a = [i for i in range(1,4) ]   #生成list a
print(a)

b = [i for i in range(100,400) if i %100 == 0]
print(b)
#列表生成是可以嵌套，此时等于两个for循环嵌套
c = [ m+n for m in a for n in b]
print(c)
#上面和下面代码一个意思
for m in a :
    for n in b :
        print(m+n,end='  ')      #两个for循环嵌套，参考九九乘法表
print()

#关于列表的常用函数
a = [x for x in range(1,100)]
#len：求列表长度
print(len(a))
#max：求列表中最大的值
#min：同理
print(max(a))
b = ['max','film','python']
print(max(b))           #这里求值的文字长度大小
#list：将其他格式的数据转换成list
a = [1,2,3]
print(list(a))
s = 'izzyxyxlove'
print(list(s))
#把range生成的内容转换成数列
print(list(range(10,20)))
