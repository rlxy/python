#收集参数混合调用案例
#stu 模拟一个学生的自我介绍
def stu(name, age, addr, *args, hobby='没有', **kwargs):
    print('大家好，自我介绍下')
    print('我叫 {0} ，我 {1} 岁了，我来自{2}。'.format(name, age,addr))
    if hobby == '没有':
        print('我没有爱好')
    else :
        print('我的爱好是{0}.'.format(hobby))
    print('#'*20)
    for i in args:
        print(i)
    print('*'*20)
    for k,v in kwargs.items():
        print(k,'--',v)
name = 'qwq'
age = 20
addr = 'china'
stu(name,age,addr)
stu(name,age,addr,hobby='python')
stu(name,age,addr, 'zyx','十九','china',hobby1='study',hobby2='python',hobby3='eat')
