# 迭代器
'''
str = '这里是迭代器'
it = iter(str)          #iter()参数填需要迭代的对象
print(next(it))                 # iter     next()
print(next(it))         #每一个next都是迭代一次it
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''
# 生成器

# 利用生成器写了个九九乘法表，并且让他按照我的意愿往下打印
'''
def jiujiu() :
    for i in range(1,10):
        for o in range(1,i+1):
            print(i * o ,end='  ')
        print()
        yield '九九乘法表第一行'                #‘yield’ 这个函数起到暂停的作用
jiujiu = jiujiu()
next(jiujiu)                                     #‘next’这个函数起到继续开始的作用
next(jiujiu)                                        #一个next打印一遍jiujiu的结果
'''


# 用生成器写出斐波那契数列

# def Fibonacci():
#     a = 0
#     b = 1
#     while True:
#         a , b = b , a+b
#         yield a
# Fibonacci = Fibonacci()
# print(next(Fibonacci))
# print(next(Fibonacci))
# print(next(Fibonacci))
# print(next(Fibonacci))



# def gen():
#     s = yield "hello"
#     print('asdsad')
#     print("用户传递进来的值为：%s" % s)
#     print('sad')
#     yield s
#
# g = gen()         #调用函数生成了一个生成器
# print(next(g))                #先调用了一次函数，打印了一个s
# print(g.send("world"))        #接下来执行这一条   send把word返回给yield，yield已经赋值给了s  然后打印调用了s，最后yield返回s


# def func():
#     for x in "ABC":
#         yield x
# for x in func():          #func里面一个生成器，每次返回一个x值，然后这里就从func里面调用一个值
# print(x)

