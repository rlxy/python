                #普通参数/位置参数
#def normal_para(one, two, three):           #定义参数时必须要和实参一对一
   # print(one + two)                        #one的实参是1，two是2
  #  return
#normal_para(1,2,3)                          #这括号里面的是实参，，，位置参数，一对上one，2对上two......

                    #默认参数案例
#def default_para(one, two, three=100):          #不给three实参的话，他就默认为100
   # print( one + two)                       #默认参数就是赋一个默认值给参数，然后如果后面给了一个实参给这个参数，那赋给那个参数的值就不要
   # return None
#default_para(1,2,3)

                   #关键字参数
#def keys_para(one, two, three):
   # print(one + two)
   # return None
#keys_para(one=1, two=2, three=3)
#为了让函数调用时不依赖参数传入的位置和顺序，则可以用这种方式参数=（实属）
#好处就是拜托了位置顺序的束缚，这么写很明白
#为了避免因为忘记参数的位置而给定义的实参输错位置，这样子可以直接用参数名给实参

                # 收集参数
#把没有位置，不能和定义时的参数位置相对于的藏书，放入一个特定的数据结构中
#参数名args不是必须这么写，但是，我们推荐直接用args，约定俗成
#参数名args前需要有星号
#收集参数可以和其他参数共存
#把关键字参数按字典格式存入收集参数
#def stu ( **kwargs):           #调用的时候需要使用关键字参数调用
#    print('下面是我的自我介绍')
#    print(type(kwargs))             #kwargs是参数的意思，一般是约定俗成
#    for k,v in kwargs.items():
#        print(k, '---', v)
#stu(name='lll',age=22,addr='china',lover='zxy',work='student')          #调用的时候把多余的关键字参数放入kwargs
#stu(name='www')                                                       #访问kwargs需要按字典格式访问
