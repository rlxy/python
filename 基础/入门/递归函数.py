#递归例子
'''
x = 0
def fun():     #定义一个函数

    global x     #因为第二次调用x的时候，x变成了局部变量，所以需要使用global提升x为全局变量
    x += 1        #每次调用一次 x 都加 1
    print(x)       #打印x

    fun()          #函数自己调用自己
fun()              #这里是调用函数，因为函数里面也有一个调用自己的式子，调用自己的时候会一直调用自己
'''
#斐波那契额例子   每一项都等于前两项之和

def fid(n):                #n表示求第n个数字的斐波那契数列的值
    if n == 1 or n == 2 :
        return 1
    return fid(n-1) + fid(n-2)
print(fid(40))                    #这里是表示第四十个斐波那契值


# 汉诺塔例子
# def hano(n,a,b,c):
#     '''
#     汉诺塔的递归实现
#     n  =第几个盘子
#     a  =代表第一个塔，开始的塔
#     b  = 代表第二个盘子，中间过渡的塔
#     c  = 代表第三个塔，目标塔
#     '''
#     if n == 1:
#        print(a,'-->',c)
#        return None
#     if n == 2:
#         print(a,'-->',b)
#         print(a,'-->',c)
#         print(b,'-->',c)
#         return None
#     #把n-1个盘子，从a塔借助c塔移到b塔上去
#     hano(n-1,a,c,b)
#     print(a,'-->',c)
#     #把n-1个盘子，从b塔借助于a塔移到c塔上去
#     hano(n-1,b,a,c)
# a = 'A'
# b = 'B'
# c = 'C'
#
# n = 100
# hano(n,a,b,c,)





