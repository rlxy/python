## zip  把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容
# zip（list1，list2）  把list1和list2里面的元素按照相同的索引位置一对一对组合放在一个元组内，多个元组组成的一个list
listname = ['xiaoyue','xiaoxin','yaoyao','xiaomeng','xiaoruan']
listscore = [45,98,54,65,12]
z = zip(listname,listscore)
print(type(z))
print(z)
for i in z:
    print(i)


##enumerate
#跟zip比较像
#对可迭代对象里面每一元素，配上一个索引，然后索引和索引内容构成一个tuple类型
l1 = [11,22,33,44,55]
em = enumerate(l1)
l2 = [i for i in em]    #给em列表里面每个元素都配上索引
print(l2)
#start 实例
em = enumerate(l1,start=100)            #start 的作用是让索引从100开始
l2 = [i for i in em]
print(l2)



#collections模块
#namedtuple
#deque

##namedtuple
#tuple类型
#是一个可命名的tuple

import collections
Point = collections.namedtuple('Point',['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])

Circle = collections.namedtuple('Circle',['x','y','r'])
c = Circle(100,150,50)
print(c)

#想检测以下namedtuple到底属于谁的子类
print(isinstance(c,tuple))


#deque    方便插入或者删除元素
from collections import deque

q = deque(['a','b','c'])
print(q)
q.append('q')       #给q列表末尾增加一个元素
print(q)
q.appendleft('x')       #给q列表最左边添加一个元素
print(q)

#defaultdict   当直接读取dict不存在的属性时，直接返回默认值
d1 = {'one':1,'tow':2,'three':3}
print(d1['one'])

from collections import defaultdict
#lambda表达式，直接返回字符串
func = lambda : '4444'      #给func定义一个数，如果下面字典打印一个未定义的值则会返回这个值
d2 = defaultdict(func)

d2['one'] = 1
d2['two'] = 2
print(d2['two'])
print(d2['ten'])        #ten这个值并没有，所以他会返回func 的那个值


#Counter   #统计字符串个数
#为什么下面结果不把括号里面的值作为键值，而是以期中每一个字母作为键值
#需要括号里的内容为可迭代
from collections import Counter
c = Counter('猜猜这里有多少值？？heihiehie')      #下面打印了括号内每一个相同键值的个数
print(c)

s = ['lxy','game','love','love','love','love','love','love','love','xy']
c = Counter(s)      #这里则打印了列表中每一个字符串的个数
print(c)







