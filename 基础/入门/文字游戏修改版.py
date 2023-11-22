import random     #使用了一个生成随机数的模块
secret = random.randint (1,100)    #这里设置了一个随机数，随机数是1到100里面的
print("文字游戏")   #游戏开始首先打印文字
temp=input("输入一个数字：")     #“input”接受了一串文本然后输出给了“temp”
guess=int(temp)         #“int”固定“temp”的输入并输出给了“guess”，“temp”等于“input("输入一个数字：")”
while guess !=secret:   #如果输入给“guess”的数字不等于系统随机生出的数字则循环运行这串代码“!=“这是不等于
    temp=input("数字不对，再来一次：")
    guess=int(temp)
    if guess == secret:    #如果输入的数字等于系统随机的数字，就执行下面的命令
        print("猜中了，真厉害")
        print("可惜猜中也没奖励")
    else:                  #否则执行“else”下面的命令
        if guess > secret:    #如果输入的数字大于随机数则执行下面的命令
            print("大了")
        else:                 #否则执行“else”下面的命令
            print ("小了")
print("结束")                  #打印一串字符


####如果需要随机多个数字出来的话，就需要用到sample模块