#包含一个学生类
#一个sayhallo函数
#一个打印语句
class student:
    def __init__(self,name='noname',age='18'):
        self.name = name
        self.age = age
    def say (self):
        print('my name is {0}'.format(self.name))
def sayhallo():
    print('这里是一个模块文件')

if __name__ == '__main__':      #一个判断语句，判断被调用的时候下面那句话是否打印
    #此判断语句作为程序入口
    print('介绍')