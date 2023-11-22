try:
    num = int(input('input your number:'))
    result = 100/num
    print('your result is {0}'.format(result))
except ZeroDivisionError as e:
    print('什么不可以当除数心里没点数？')
    print('ZeroDivisionError：{0}'.format(e))
except NameError as e:
    print('应该是语法错误')
    print('NameError:{0}'.format(e))
except ValueError as e :
    print('输错了')
    print(e)

# 所有的异常都是继承于Exception
# 任何异常都能拦截住
#这应该是最后一个exception，因为写下去没有意义
except Exception as e :

    print('我也不知道出什么错误了')
    print(e)
finally:
    print('这句话不管有没有异常都执行')