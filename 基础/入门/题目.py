'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j )and(j != k )and(k != i) :
                print(i,j,k)
'''         #不重复的三位数
'''
temp =input('请输入一个整数')
number = int(temp)
i = 1
while number:
    print(i)
    i += 1
    number +=1
'''         #依次加一，无限循环
'''
for i in range(1,5):
    for k in range(1,5):
        for o in range(1,5):
            for l in range(1,5):
               if ( i != k ) and ( i != o ) and ( i != l ) and ( k != o ) and ( k != l ) and ( o != l ):
                   print(i,k,o,l)
'''         #不重复的四位数
'''
for i in range(1,168):
    if 168 % i ==0 :
        j = 168 /i
        if i > j and (i+j) % 2 == 0 and(i-j) %2 ==0:
            m = (i+j)/2
            n = (i-j)/2
            x = n * n - 100
            print( x )
'''         #一个整数加100是一个平方根，再加168还是一个平方根
'''
a = (int(input('输入a：')))
b = (int(input('输入b：')))
c = (int(input('输入c：')))
d = (int(input('输入d：')))
print(a + b - c * d)
'''         #输入a,b,c,d4个整数，计算a+b-c*d的结果
'''
a = int(input('请输入矩形长度：'))
b = int(input('请输入矩形宽度：'))
print('面积')
print(a * b)
print('周长')
print((a + b) *2)
'''         #输入值，计算矩形面积和周长
'''
float = 9/2
print(float)
'''         #计算9/4的小数结果
'''
print(7*7*7*7)
print(7**4)
print(pow(7,4))
print(eval('%s*%s*%s*%s'%(7,7,7,7)))
a = 7
for i in range(3):
    a *=7
'''         #计算7*7*7*7的写法
"""
for i in range(1,10):
    for j in range(1,i+1):
        print('''%d*%d=%d'''%(i,j,i*j) ,end=' ')     #使用最传统的格式化
    print()
"""         #九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        k =  i * j
        print("{}*{}={}".format(j,i,k),end='  ') #这里使用format格式化
    print('')
'''         #九九乘法表2
'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(35))
'''         #斐波那契数列
'''
import time
l =[1,2,3,4,5,6,8,9]
for i in range(len(l)):
    print(l[i])
    time.sleep(1)
'''         #暂停一秒输出
'''
print(sorted([int(input("请输入一个整数："))for x in range(3)]))
#sorted 这个函数是排序命令。
# input输出值给int，int转换数字给sorted，for循环三次，所以就输出三次值给sorted，随后就是sorted排序
'''         #排序
'''
l=[]
for i in range(3):
    x = int(input('输入一个数字：'))
    l.append(x)         
l.sort()            #sort是给一个列表排序，默认从小到大
print(l)
'''         #排序2
'''
for i in range(100,1000):
    j = i // 100
    k = i // 10 %10
    l = i % 10
    if i == (j ** 3 + k **3 + l **3):
        print(i)
'''         #水仙花数
'''
string = input('请输入一串字符：')
英文 = 0
空格 = 0
数字 = 0
其他 = 0
for a in string :
    if a.isalpha():
        英文 += 1
    elif a.isspace():
        空格 += 1
    elif a.isnumeric():
        数字 += 1
    else:
        其他 += 1

print('英文 = %s，空格 = %s，数字 = %s，其他 = %s'%(英文,空格,数字,其他))
'''         #求字符串里面字符类型的个数
'''
n = int(input('请输入层数：'))
a = int(input('请输入计算数：'))
su = 0
tu = []
for i in range (n):
    tu.append(int(str(a) * (i+1)))
print('创建的列数为：%s'% tu)
for i in (tu) :
    su += i
print('数列的和：%s'%su)
'''         #求s=a+aa+aaa+aaaa......
'''
print('=' * 20)
name = input('姓名：')
qq = input('QQ：')
num = input('手机号： ')
d = input('公司地址：')
print('=' * 20)


user = input('请输入用户名：')
if user == 'admin' :
    passwd = input('请输入密码：')
    if passwd == '123456':
        print('欢迎登录')
    else :
            print('密码错误')
else :
    print('用户名不存在')
'''         #登录
'''
x = 0
for i in range(1,101) :
    x +=i
    print(x)

i = int(input('请输入整数：'))
I = int(input('请输入整数：'))
print(i + I)
'''         #一百内整数相加
'''
# 一个球,从200米高空落下,第一个回弹190米,第二次回弹180米,第三次回弹170米,当球不在弹时,求 球一共运行了多少米

# ht = t = 0
# g = 200
#
# while g > 0 :
#     t += g
#     g -=10
#     ht +=g
#     z = ht + t
# print(t)
# print(ht)
# print(z)


a = 200
b = True
k=l=s=0
while b:
	s+=a #弹下的路径
	a=a-10
	k+=a # 回弹的路径
	l=k+s
	if a<=0:
		print('不回弹的米数是:%d,回弹的米数是:%0d,一共有:%0d米'%(s,k,l))
		b=False
'''         #计算球弹的米数
'''
number = int(input('输入需要因式分解的数字:'))
l = [ ]

while number != 1 :
    for i in range (2,number+1):
        if number % i == 0 :
            l.append(i)
            number /= i

print(l)
##################################################
x = int(input('输入一个数字:'))
while(x) :
    n = int(input('请输入一个正整数进行因式分解:'))
    print('%d = ' %n, end=' ')
    while n not in [1] :
        for i in range(2,n+1):
            if n % i == 0 :
                n =int(n/i)
                if n == 1 :
                    print('%d ' %i,end=' ')
                else :
                    print('%d *' %i,end=' ')
                break
    print()
'''         #因式分解
'''
l = []

for x in range (1,1001):
    a = []
    for i in range(1,int(x/2+1)) :
        if x % i == 0:
            a.append(i)
    if x == sum(a):
        print(x)
        print(a)
        l.append(x)
        print('完数共有%d个'%len(a))
'''         #计算一千以内的完数
'''
year = int(input('请输入需要判断的年份：'))

if year % 4 == 0 and year % 100 !=0 :
    print('这是闰年')
else :
    print('这是平年')
'''         #判断年份
'''
num = int(input('请输入需要判断的数字：'))
if num %2 ==0 :
    print('这是偶数')
else :
    print('这是奇数')
'''         #判断奇偶数
'''
l = []
x = []
for i in range(0,101) :
    if i % 2 != 0 :
        l.append(i)
    else :
        x.append(i)
print(l)
'''         #写出0-1爱因斯坦数学题
'''
for red in range(0,4):
    for yellow in range(0,4):
        for blue in range(2,7):
            if red+yellow+blue == 8 :
                print(red,'\t',yellow,'\t',blue)
'''         #三色球问题00的奇数
'''
l = []
n = []
for i in range(7,10000):
    if(i % 2 == 1) and (i % 3 == 2) and (i % 5 == 4) and (i % 6 == 5)and(i % 7 ==0):
        l.append(i)
    else :
        n.append(i)
print(l)
print(n)

# x = 7
# i = 1
# flag = 0
# while i < 100:
#     if(x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5):
#         flag = 1
#     else :
#         x = 7 *(i+1)
#     i +=1
# if flag == 1:
#     print('这个数字是',x)
# else:
#     print('找不到')
'''         #
'''
for i in range(1,1001):
    num = 0
    for l in range(1,i):
        if i % l ==0:
            num +=l
            if num == i :
                print(i)
'''         #找出1000以内的所有完数
'''
h = 100
l = 100
for i in range(2,11) :
    h /=2
    l += (h*2)
    if i == 10:
        print(h)
print(l)
'''         #一球从100米高度自由落下
'''
remain = 1
for i in range(1,10):
    remain = (remain+1)*2
    if i ==10 :
        remain -=1
print(remain)
'''         #猴子吃桃问题
'''
for a in ('x','y','z'):
    for b in ('x', 'y', 'z'):
        for c in ('x', 'y', 'z'):
            if (a!= b)and(b!=c)and(a!=c)and(a!='x')and(c!= 'x')and(c!= 'z'):
                print('a 和 %s,b 和 %s，c 和 %s'%(a,b,c))
'''         #乒乓球队比赛

























































































































