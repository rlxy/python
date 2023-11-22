"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：全局变量和局部变量，局部变量提升为全局变量操作(global)，eval()函数和exec()函数案例
"""

'''
a1 = 100            #这里a1是全局的作用域
def fun ():
    print(a1)
    print('i am in fun')
    a2 = 99            #这里a2是算总局部的作用域
    print(a2)
print(a1)    #这里的a1是作用全局的，上面定义的那个a1也是全局，所以可用
fun()           #这个函数里面所定义的就在一个作用域
#print(a2)     #如果打印这个a2，就报错，因为上面定义的a2是局部的，这里的a2是全局的
'''
# 这下面是一个提升局部变量为全局变量，使用global

a3 = 888
def fun ():
    print(a3)
    print('i am in fun')
    global a4
    a4 = 777        #a4本来是局部变量，上面使用了global提升成为全局变量
    print(a4)
print(a3)
fun()
print(a4)              #此时a4已经提升成了全局变量，可以输出
#如果print(a4)放在fun（）的前面则会报错，因为a4在fun（）前并没有赋值，a4是在fun（）里面赋值先
#所以a4放在函数前面打印的话会报错，fun（）之前并没有给a4任何赋值

    # eval()函数和exec()函数案例
 # eval()
'''
x = 100
y = 200
z1 = x + y
z2 = eval('x+y')       #把字符串当一个表达式来执行
print(z1)
print(z2)                 #eval返回结果
'''
# exec()案例
'''
x = 100
y = 200
z1 = x + y
z2 = exec("print('x+y:',x+y)")   #注意字符串中引号的写法，比对exec执行结果和代码执行结果
print(z1)
print(z2)                #exec不返回结果
'''