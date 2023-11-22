class NonexistentErrors(NameError):                 #自己定义一个Error继承于NameError
    pass                           #自己定义的错误有好处就是， 这个类里面可以自己加其他的代码

try :
    print('这里正常')
    print('这里也没问题')
    raise NonexistentErrors                 #执行了自己定义的错误，接下来会返回到哪一个错误上？
    print('并不执行')
except NameError as e :                    #因为继承于NameError，所以，会跳到NameError错误上面
    print('出现了一个NameError')
    print('Manually raised exception')
    print(e)
except Exception as e :
    print('出了一个意料之外的异常')
    print(e)
finally :
    print('我肯定是会被执行的')

'''    
关于自定义异常
    -只要是raise异常，则推荐自定义异常
    -在自定义异常的时候，一般包含以下内容：
        自定义发生异常的代码
        自定义发生异常后的问题提示
        自定义发生异常的行数
    -最终的目的是，一旦发生异常，方便快速定位错误现场
'''