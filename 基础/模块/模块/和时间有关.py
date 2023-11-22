
# -timezone  当前时区和UTC时间相差的秒数，在没有夏令时情况下的间隔,我们这里是东八区
import time
import datetime
import timeit


print(time.timezone)        #2019/08/05 测试为-28800

# -altzone    获取当前时区与UTC时间相差的秒数，在有夏令时的情况下
print(time.altzone)         #2019/08/05 测试为-32400

# -daylight 测当前是否是夏令时时间状态 0 表示是
print(time.daylight)

# time      得到时间戳  获得当前与1970年到现在多少秒
print(time.time())

# localtime  得到当前时间的时间结构
# asctime() 返回元组的正常字符串化之后的时间格式
t = time.localtime()
tt = time.asctime(t)
print(t)        #也可以单独打印 print(t.时间属性)
print(tt)

# ctime()  直接获取字符串化的当前时间
t = time.ctime()
print(t)

# mktime() 使用时间元组获取对应的时间戳        返回的浮点数的时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(ts)

# clock 获取cpu时间， 3.0-3.3版本直接使用，其他版本调用有问题

# sleep  使程序进入睡眠，n秒后继续
for i in range(10):
    print(i)
    time.sleep(0.1)       #每完成一次循环则停顿0.1秒
'''
#-strftime  将时间元组转化为自定义的字符串格式
t = time.localtime()
ti = time.strftime('%Y年%m月%d日 %H:%M',t)             #这里报编译错误
print(ti)
'''


#datetime 模块


#data           #返回一个理想的日期，提供year，month,day属性
dt = datetime.date(2019,8,6)
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)

#time    提供一个理想的时间，居于hour,minute,second,microsec等内容
dt = datetime.time(8,25,12)
print(dt.hour)
print(dt.minute)
print(dt.second)

#datetime   提供日期跟时间的组合
#常用类方法
#today     今天的时间
#now       现在的时间
#utcnow    utc世界标准时间
#fromtimestamp  从时间戳里面返回本地时间
dd = datetime.datetime(2019,8,6)
print(dd.today())
print(dd.now())
print(dd.utcnow())
print(dd.fromtimestamp(time.time()))

#timedelta  表示一个时间间隔
tl = datetime.datetime.now()
print(tl.strftime('%Y - %m - %d  %H:%M:%S'))
td = datetime.timedelta(hours=1)        #表示时间间隔增加一小时
print((tl + td).strftime('%Y - %m - %d  %H:%M:%S'))       #tl时间加上td的时间间隔



#timeit 时间测量工具


#测量程序运行时间间隔实验
def p():
    time.sleep(3.3)
tt = time.time()    #第一个时间的时间戳
p()                 #调用p()函数
print('使用sleep:{0}'.format(time.time() - tt))     #用现在的时间戳 减 上一个时间戳


#生成列表两种方法的运行时间比较
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
#利用timeit调用代码执行100000次，查看运行时间
t1 = timeit.timeit(stmt='[i for i in range(1000)]',number=100000)       #运行一个同样的程序，运行100000次
t2 = timeit.timeit(stmt = c,number=100000)
print('c代码运行的时间：{0}'.format(t1))
print('tl里面代码运行的时间：{0}'.format(t2))

#timeit 可以执行一个函数，来测量一个函数的执行时间
def d():
    num = 3
    for i in range(num):
        print('repeat : {0}'.format(i))
t = timeit.timeit(stmt=d,number=10)
print('这个函数运行了{0}s时间'.format(t))

s = '''
def d(num):
    for i in range(num):
        print('repeat : {0}'.format(i))
'''
#执行d（num）
#setup负责把环境变量准备好
#实际相当于给timeit创造了一个小环境
#在创作的小环境中，代码执行的顺序大致是
'''
def d(num):
    ......
num = 3
d(num)      
'''

t = timeit.timeit('d(num)',setup=s+'num=3',number=10)
print('这个函数运行了{0}'.format(t))






'''
                        strftime所使用的格式
格式        含义   
%a          本地（locale）简化星期名称
%A          本地完整星 期名称
%b          本地简化月份名称
%B          本地完整月份名称
%C          本地相应的日期和时间表示
%d          -个月中的第几天(01 - 31)
%H          -天中的第几个小时(24 小时制，00一23)
%I          -天中的第几个小时(12 小时制，01一12)
%j          一年中的第几天(001 - 366)
%m          月份(01一12)
%M          分钟数(00 - 59)
%p          本地am或者pm的相应符  注1
%S          秒(01- 61)  注2
%U          -年中的星期数(00 一53星期天是一一个星期的开始)第-一个星期天之前的所有天数都放在
%w          -个星期中的第几天(0一6，0是星期天)注3
%W          和%U基本相同，不同的是%W以星期一为一一个星期的开始
%x          本地相应日期
%X          本地相应时间
%y          去掉世纪的年份(00 - 99)
%Y          完整的年份
%Z          用+HHMM 或- HHMM表示距离格林威治的时区偏移(H 代表十进制的小时数，M代表十进制
%%          %号本身
'''


'''
### 时间戳
    -一个时间表示，根据不同语言，可以是整数或者浮点数
    -是从1970年1月1日0时0分0秒到现在经历的秒数
    -如果表示的时间时1970年以前或者太遥远的未来，可能出现差异
    -32位操作系统能够支持到2038年
    
### UTC时间
    -UTC时间又称世界协调时间，以英国的格林尼治天文所在地区的时间作为参考
    的时间，也叫做世界标准时间
    -中国时间时 UTC+8 东八区
    
### 夏令时
    -夏令时就是在夏天的时候将时间调快一小时，本意督促大家早睡早起节省蜡烛！
    每天变成25个小时，本质没变还是24小时
    
### 时间元组    
-一个包含时间内容的普通元组
索引        内容         属性          值

0          年          tm_year        2015
1          月          tm_mon         1 - 12
2          日          tm_mday        1 - 31
3          时          tm_hour        0 - 23
4          分          tm_min         0 - 59
5          秒          tm_sec         0 - 61 60表示闰秒，61保留值
6          周几        tm_wday        0 - 6
7          第几天      tm_yday        1 - 366
8          夏令时      tm_isdst       0 ,1, -1 （表示夏令时）
'''






