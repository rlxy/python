"""
Filename: 函数编程.py
Author: 药药
Contact: 1579954422@qq.com
introduce：lambda表达式，高阶函数，归并，过滤，排序，返回函数，闭包
"""
# python语言的高级特性

##函数式编程（FunctionalProgramming）
# 基于lambda演算的一种编程方式
# 程序中只有函数
# 函数可以作为参数，同样可以作为返回值
# 纯函数式编程语言：LISP ，Haskell
# Python函数式编程只是借鉴函数式编程的一些特性，可以理解成一半函数式一半Python
# 内容
    # 高阶函数
    # 返回函数
    # 匿名函数
    # 装饰器
    # 偏函数

## lambda 表达式
# 函数: 最大程度复用代码
# 存在问题：如果函数很小，很短，则会造成啰嗦

# lambda表达式（匿名函数） :
# 一个表达式，函数体相对简单
# 不是一个代码块，仅仅是一个表达式
# 可以有参数，有多个参数也可以，用逗号隔开
# lambda 表达式用法
    # 1 ， 以lambda开头
    # 2 ， 紧跟一定的参数（如果有的话）
    # 3 ， 参数后用冒号和表达式主题隔开
    # 4 ， 只是一个表达式，所以，没有teturn

# 实例 ： 计算一个数字的100倍
stm = lambda x: 100 * x
print(stm(99))

stm2 = lambda x, y, z: x + y * 10 + z * 100
print(stm2(3, 4, 5))

# 高阶函数
# 把函数作为参数使用的函数，叫高阶函数

a = 100
b = a

# 函数名称就是一个变量
def funA():
    print('in funA')


funB = funA
print(funB())


##结论
# 函数名称也是变量
# funB 和funA只是名称不一样而已
# 既然函数名称是变量，则应该可以被当作参数传入另一个函数

##高阶函数
# funA 是普通函数，传入数字的100倍数字
def funA(n):
    return n * 100


# 再写一个函数，把传入参数乘以300倍
def funB(n):
    # 最终是返回30000
    return funA(n) * 3  # 上面funA的n参数没有赋值，到funB在赋值


print(funB(10))


# 写一个高阶函数
def funC(n, f):
    # 假定函数是把n扩大100倍
    return f(n) * 3


print(funC(9, funA))


# 相比较funC和funB， 显然funC的写法要优于funB
# 例如 ：
def funD(n):
    return n * 10


print(funC(7, (funD)))

###系统高阶函数 - map
# 原意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
# map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象
# 用map把一个列表中的每个元素乘以10并得到新的列表
l1 = [i for i in range(10)]
l3 = []


def mulTen(n):
    return n * 10


l3 = map(mulTen, l1)
l4 = []
# map类型是一个可迭代函数，所以可以用for循环遍历
for i in l3:
    l4.append(i)
print(l4)

# 高阶函数 - 归并
##reduce
# 原意式归并，缩减
# 把一个可迭代对象最后归并成一个结果
# 对于作为参数的函数要求 ：必须有两个参数，必须返回结果
# reduce([1,2,3,4,5]) == f(f(f(f(1,2)),3),4),5)           后面相当于嵌套
# reduce需要导入functools包
from functools import reduce


# 定义一个操作函数
def myadd(x, y):
    return x + y


# 对于列表[1,2,3,4,5,6]执行myadd的reduce
rst = reduce(myadd, [1, 2, 3, 4, 5, 6])  # 把列表里面所有元素相加
print(rst)


# 高阶函数 - 过滤
# filter 函数
# 过滤函数： 对一组数据进行过滤，符合条件的数据会生成一个新的列表返回
# 跟map相比较
# 相同：都会对列表的每一个元素逐一进行操作
# 不同：
# map会生成一个跟原来数据相对应的新列表
# filter不一定，只要符合条件的才会进入新的数据集合
# filter 函数怎么写
# 利用给定函数进行判断
# 返回值一定式个布尔值
# 调用格式：filter（f，data），f式过滤函数，data式函数
# 函数
# 对于一个列表，对其进行过滤，偶数组成一个新列表

# 需要定义过滤函数
# 过滤函数要求有输入，返回布尔值
def isEven(a):
    return a % 2 == 0


l = [5, 65, 4, 56, 879, 545, 1, 41, 6, 4, 8, 94, 6, 2]
rst = filter(isEven, l)
print([i for i in rst])

##高阶函数 - 排序

# 把一个列表按照给定算法进行排序
# key：在排序前对每个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排序

a = [456, 789, 6, 35, 46, 89, 21]
al = sorted(a, reverse=False)  # 后面是False是顺序，Ture是倒序    默认的就是顺序
print(al)

# 排序2
# sorted(list,[key=type])
# 按照绝对值进行排序
# avs是求绝对值
# 按照绝对值的倒叙进行排列
b = [-45, -84, 84, 645, -562, -541, 456, 321]
all = sorted(b, key=abs, reverse=True)
print(all)

# sorted排序  字符串排序
astr = ['lxy', 'YSL', 'armani', 'Dior', 'Balenciaga']
str1 = sorted(astr)
print(str1)
# str.lower 是小写的意思
str2 = sorted(astr, key=str.lower)
print(str2)


##返回函数
# 函数可以返回具体的值
# 也可以返回一个函数作为结果
# 定义一个普通函数
def myF(a):
    print('in myF')
    return None


a = myF(8)
print(a)


def myF2():
    def myF3():
        print('函数嵌套')
        return 3

    return myF3


# 使用上面定义
# 调用myF2，返回一个函数myF3，赋值给f3
f3 = myF2()
print(f3())


# 复杂一点的返回函数的例子
# args ： 参数
# *args 代表myF4函数的参数
# 1 myF4定义函数，返回内部定义的函数myF5
# 2 . myF5使用了外部变量，这个变量是myF4的参数

def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst

    return myF5


f5 = myF4(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# f5的调用
print(f5())

f6 = myF4(10, 20, 30, 40, 50)
# f5的调用
print(f6())


##闭包（closure）
# 当一个函数在内部定义函数，并且内部的函数应用外部函数的参数或者局部变量，
# 当内部函数被当作返回值的时候，相关参数和变量保存在返回的函数中，这种结果叫闭包
# 上面定义的myF4是一个标准闭包结构

# 闭包常见坑
def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 出现的问题 ：
# 造成上述状况的原因是，返回函数引用了变量i ， i并非立即执行，而是等到三个函数都返回的时候才统一使用，此时i已经变成了3.
# 最终调用的时候，都返回的是3*3
# 此问题说明  返回闭包时，返回函数不能引用任何循环变量
# 解决方案 ： 再建一个函数，使用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何改变，已绑定的函数参数值不再改变
# 修改上述函数
# 闭包常见坑
def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count2()
print(f1())
print(f2())
print(f3())
