"""
Filename: 协程.py
Author: 药药
Contact: 1579954422@qq.com
introduce：
"""
# 协程
# 迭代器
# 可迭代（Iterable）: 直接作用于For循环的变量”,
# 迭代器（）：不但可以作用于for循环，还可以被next调用”,
# list是一个典型的可以迭代对象，但不是迭代器”,
# 通过isinstance判断”,
# iterable 和 iterator可以转换”,
# 通过 iter函数可以进行转换”
# # 可迭代,
l = [i for i in range(10)]

# l 是一个可迭代的对象，但不是迭代器",
for idx in l:
    print(idx)

# range是一个迭代器,
for i in range(2):
    print(i)


# isinstance案例,
# 判断某个变量是否是一个实例,

# 判断是否可迭代,
from collections import Iterable

ll = [1,2,3,4,5]
print(isinstance(ll,Iterable))
# 结果为True ll为可迭代的对象

from collections import Iterator

print(isinstance(ll,Iterator))
# 结果为false 说明 ll不是迭代器


# iter函数

s = "I love You"

print(isinstance(s,Iterable))
print(isinstance(s,Iterator))

s_iter = iter(s)

print(isinstance(s_iter,Iterable))
print(isinstance(s_iter,Iterator))



# 生成器,
# generator : 一边循环一边计算下一个元素的机制／算法
# 需要满足三个条件
# 每次调用都生产出for 循环需要的下一个元素
# 如果达到最后一个后，爆出StopIteration异常
# 可以被next函数调用
# 如何生成一个生成器
# 直接使用
# 如果函数中包含yield，则这个函数就叫做生成器
# next 调用函数，遇到yield返回
# 直接使用生成器

L = [x*x for x in range(5)] # 放在中括号中的列表生成器
g = (x*x for x in range(5)) # 放在小括号中的就是生成器

print(type(L))
print(type(g))


# 函数案例
# 在函数odd中，yield负责返回
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3

# odd()是调用生成器，通过next进行调用
g = odd()
one = next(g)
print(one)
two = next(g)
print(two)
three = next(g)
print(three)

# 通过for 循环调用生成器
# 斐波那契数列生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n += 1
    return 'Done'
g = fib(5)

for i in range(6):
    rst = next(g)
    print(rst)





ge = fib(10)
""",
生成器的典型用法是在for 循环中使用,
比较常用的典型生成器就是range,
"""
for i in ge:
    print(i)

# 协程,
    # 历史历程,
        # 3.4 引入协程，用yield实现,
        # 3.5 引入协程语法,
            # 实现的协程比较好的包有asyncio, tornado,gevent,
    # 定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序。,
        # 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成一个协程的生成器,
    # 协程的实现,
        # yield返回,
        # send调用,
    # 协程的四个状态,
    # inspect.getgeneratorstate(…) 函数确认，该函数会返回下述字符串的一个：,
        # GEN_CREATED：等待开始执行,
        # GEN_RUNNING：解释器正在执行,
        # GEN_SUSPENED：在yield表达式处暂停,
        # GEN_CLOSED：执行结束,
    # next预计（prime）,
    # 协程终止,
# 协程中未处理的异常会向上冒泡，传给next函数或者send函数的调用方,
# 终止协议的一个方式：发送某个哨符值，让协程退出，内置的None 和Ellipsis等常量经常作用哨符值。,
# yield from,
    # 调用协程为了得到返回值，协程必须正常终止,
    # 生成器正常终止会发出StopIteration异常，异常对象的value属性保存返回值,
    # yield form从内部捕获StopIteration异常”
    # 委派生成器
        # 包含yield from 表达式的生成器函数
        # 委派生成器在yield from表达式处暂停，调用方可以直接把数据发给子生成器
        # 子生成器在把产生的值发给调用方
        # 子生成器在最后，解释器会抛出StopIteration，并且把返回值附加到异常对象上。
# 协程代码案例1
def simple_coroutine():
    print("-> start")
    x = yield
    print("-> recived",x)

# 主线程
sc = simple_coroutine()
print(111)
# 可以使用sc,send(None),效果一样
next(sc) # 预计
print(222)
sc.send("Zhexiao")# 主进程给协程发一个信号"

# 案例2协程的状态

def simple_coroutine(a):
    print("-> start")

    b = yield a
    print("-> recived",a,b)

    c = yield a + b
    print("-> recived",a,b,c)

# runs

sc = simple_coroutine(5)

aa = next(sc)
print(aa)
bb = sc.send(6)
print(bb)
cc = sc.send(7)
print(cc)




def gen():
    for c in "AB":
        yield c

# list 直接用生成器作为参数
print(list(gen()))

def gen_new():
    yield from "AB" # yield from 相当于通道。

print(list(gen_new()))

# 委派生成器
from collections import namedtuple
"""
解释：
    1、外出for 循环每次迭代会新建立一个grouper 实例，赋值coroutine变量；
    2、激活协程
    3、内层for循环变量字典value值，并将该value发送给协程，进行平均值计算；
    4、发送哨兵，终止协程，打印计算结果
"""

ResClass = namedtuple("Res","count average")

# 子生成器
def averager():
        total = 0.0
        count = 0
        average = None

        while True:
            term = yield
            if term is None:
                break
            total += term
            count += 1
            average = total / count
        return ResClass(count, average)

# 委派生成器
def grouper(storages, key):
    while True:
        # 获取averager()返回值
        storages[key] = yield from averager()

# 客户端代码
def clinet():
    process_data = {
        'boys_1' : [20,18,12,32,333,43,432],
        'boys_2' : [123,321,32123,3223,423,4232,23]
    }

    storages = {}

    for k,v in process_data.items():
        # 获得协程
        coroutine = grouper(storages,k)

        #预激协程
        next(coroutine)
        #发送数据到协程
        for dt in v:
            coroutine.send(dt)

        #终止协程
        coroutine.send(None)
    print(storages)

#run
clinet()
