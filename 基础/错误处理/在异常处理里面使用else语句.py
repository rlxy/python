try :
    num = int(input('输入一个能除100的数字：'))
    result = 100 / num
    print('结果为：{0}'.format(result))
except Exception as e :         #有任何错误执行这里
    print('Exception ')
else:                       #否则执行这里
    print('No Exception')
finally:                       #不管怎么样肯定会执行这里
    print('肯定会被执行')
