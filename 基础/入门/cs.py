"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：input，print，if else，while函数使用，各种符号使用，二目和三目写法，一个简单文字小游戏
"""

'''
name = input('请输入名字：')
print('你好，'+name+'!')
'''
'''
temp = input('输入1到100的数字：')
num =int(temp)
if 1 <= num <= 100 :
    print('111')
else :
    print('123')
'''
'''
while 'C' :         #这里没有明确的循环次数或者限制，所以是无限循环
    print('d')
'''
'''
i = 10
while i :
    print('123456')
    i -=1              #每次循环都减1，上面i赋值是10，所以能减十次，也就是可以循环10次
'''
'''
cost = 5
l = 10 < cost               #这里是二幕写法
x = cost < 20               #三幕写法：10 < cost < 50
print(l,x)
'''
'''
i = 1.6
print(int(i))      #浮点类型化为整数的时候都会不是四舍五入，而是保留小一位
'''

'''import random
times = 3
secret = random.randint(1, 100)
print("文字游戏")
guess = 10
print("输入一个数字：", end='')
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input('输入有误，重新输入：')
    guess = int(temp)
    times -= 1
    if guess == secret:
        print("猜中了，真厉害")
        print("可惜猜中也没奖励")
    else:
        if guess > secret:
                print("大了")
        else:
                print("小了")
        if times > 0:
                print('再来一次吧：')
        else:
                print('机会用完了！')
print("结束")'''
