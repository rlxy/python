import random
secret = random.randint (1,100)
print("文字游戏")
temp=input("输入一个数字：")
guess=int(temp)
i = 3
while guess !=secret:
    i -=1
    if i == 0:
        break
    else:
        temp=input("错了，再来一次：")
        guess=int(temp)

        if guess == secret:
            print("猜中了，真厉害")
            print("可惜猜中也没奖励")
        else:
            if guess>secret:
                 print("大了一点")
            else:
                 print("小了")
print("游戏结束")

