#调式技术
#调试流程：单元测试-》集成测试-》交测调试
#分类：
    #静态调试：
    #动态调试：
#pdb调试
#pdb ：python调试库

#pycharm调试
#run/debug模式
#断点：程序的某一行，程序debug模式下，遇到断点就会暂停
def sayhallo(name):
    print('i want to say hello with you,{0}'.format(name))
    print('hello,{0}'.format(name))
    print('done.......')

if __name__ == '__main__' :
    print('***'*10)
    print('***'*10)     #单继行号的后面 出现红点 ，红点这里就是断点   运行debug   到断点这里会暂停  等待运行下一行
    print('///'*10)
    name = input('please input your name :')
    print(sayhallo(name=name))
    print('@@@'*10)






