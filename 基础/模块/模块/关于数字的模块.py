import random
# random 随机数
# 所有的随即模块都是伪随机
#random（） 获取0-1之间的随机小数
#格式：random.random（）
print(random.random())


#choice() 随机返回序列中的某个值
#格式：random.choice（序列）
l = [(str(i) + 'haha') for i in range(10)]
print(l)
rst = random.choice(l)     #随机生成l列表中的一个值
print(rst)


#shuffle()  随机打乱列表
#格式 : random.shuffle(列表)
print(random.shuffle(l))
print(l)


#randint(需要随机的范围)  随机生成一个括号范围内的整数
print(random.randint(0,100))






