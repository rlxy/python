#普通函数调用
def hallo():
    print('hallo,word')
    return 1
f = hallo
#f和hallo是同一个函数
print(f())

#如果需要在不修改原来代码的情况下 每次对hallo调用的时候打印当前系统时间
#这么做需要使用装饰器

##装饰器（Decrator）
#在不改动代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数
#装饰器的使用：使用@语法，即在每次要扩展到函数定义前使用@+函数名
#任务 ：
#对hello函数进行功能扩展，每次执行hello打印印当前时间
import time

#高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args,**kwargs):
        print('Time:',time.ctime())
        return f(*args,**kwargs)
    return wrapper
#上面定义了装饰器，使用的时候需要用到@，此符号是python的语法糖
@printTime
def hello():
    print('hello,word')
print(hello())

#装饰器的好处是，一点定义则可以装饰任意函数
#一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上

@printTime
def hello2():
    print('装饰器的使用实例2')
    print('装饰器这么用')
print(hello2())

#上面对函数的装饰使用了系统定义的语法糖
#下面开始手动执行下面装饰器
#先定义函数
def hello3():
    print('这里使用手动执行试试')
hello3 = printTime(hello3)
print(hello3())
f = printTime(hello3)
printTime(f())          #这里打印了两个时间  因为上面hello3 已经执行了 hello3 = printTime(hello3)  这里执行一遍装饰器  f执行一遍 就打印2个了

#偏函数
#把字符串转化成十进制
# int = int('12345')
# print(int)
#求八进制的字符串12345，表示成十进制的数字是多少
# int = int('12345',base=8)
# print(int)

#新建一个函数，此函数是默认输入的字符串是16进制数字
#把此字符串返回十进制的数字
# def int16(x,base=16):
#     return int(x,base)
# print(int16('12345'))

##偏函数
#参数固定的函数，相当于一个由特定参数的函数体
#functools.partial的作用是，把一个函数某些函数固定，返回一个新函数
import functools
#实现上一个int16的功能
int16 = functools.partial(int,base=16)
print(int16('12345'))



