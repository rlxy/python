try :
    print('这里正常')
    print('这里也没问题')
    raise NameError         #raise 是用来引发一个异常，语法  raise ErrorClassName
    print('这句话执行了，因为上面扔了一个异常直接跳到下面的异常处理')
except  NameError as e :
    print('出现了一个NameError')
    print('Manually raised exception')
    print(e)
except Exception as e :
    print('出了一个意料之外的异常')
    print(e)
finally :
    print('我肯定是会被执行的')