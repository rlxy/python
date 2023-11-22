class student:
    def __init__(self,name='noname',age='18'):
        self.name = name
        self.age = age
    def say (self):
        print('my name is {0}'.format(self.name))
def sayhallo():
    print('这里是一个模块文件')
print('这是模块p01')