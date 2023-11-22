"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：面向对象的使用，定义类，对象属性，关于self，调用绑定类函数使用类名，关于self的案例（鸭子类型），
私有变量，继承，子类扩充父类，多继承，扩展构造函数，构造函数的调用，构造函数概念，类相关的函数，peroperty案例，
属性操作(getattr)，操作类的函数，属性操作相关，因为setattr造成的死循环，进行大于判断时候触发，
类和对象的三种方法，属性的三种用法，类属性property，抽象，抽象类的使用，函数当变量使用，自己组装一个类，
组装类例子(借用types.MethodType来直接绑定实例)，利用type造一个类，元类演示
"""
# 定义一个学生类，用来形容学生
'''
#定义一个空的类
class Student():
    #一个空类，pass代表直接跳过
    #此处pass必须有
    pass

#定义一个对象
lll = Student()

#在定义一个类，用来描述听Python的学生
class PythonStudent():
    name = None
    age = 18
    course = 'Python'

#需要注意
    #1，def doHomework 的缩进层级
    #2，系统默认有一个self参数
    def doHomework(self):
        print('do work')
        print('my age is ',yy.age)

        #推荐在函数末尾使用return语句
        return None

#实例化一个叫yy的学生，是一个具体的人
yy = PythonStudent()
print(yy.name)
print(yy.age)
#注意成员函数的调用没有传递进入参数
yy.doHomework()
 '''        # 面向对象

'''
class Sutdent():        #这里定义了一个Sutdent类，下面是这个学生类所拥有的名字，年龄
    name = 'lll'           #这里的都是属性
    age = 18
Sutdent.__dict__
#实例化
yueyue = Sutdent()      #这个成员可以归‘yueyue’这个对象所拥有
yueyue.__dict__
'''         # 定义一个类

'''
class A():       #定义一个类
    name = 'ZZZ'    #这些时A类的属性
    age = 18
    #注意say的写法，参数有一个self
    def say(self):
        self.name = 'aaa'
        self.age = 10
        self.home = 'qq'
#此案列说明
#类实列的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量

#A称为类实列
print(A.name)
print(A.age)
print(id(A.name))            #id 可以鉴别一个变量是否和另一个变量是同一变量
print(id(A.age))
print('-' * 20)
a = A
print(a.name)
print(a.age)
print(id(a.name))           #这里两组数据的id和上面两组一样，所以处于同一变量
print(id(a.age))
print('-' * 20)

a = A()
a.name = 'yyy'
a.age = 16
print(a.name)
print(a.age)
print(id(a.name))           #id不同，因为这是对象a中添加的成员，不是属于类中的成员
print(id(a.age))
'''         # 实例对象属性



"""
class Student():
        name = 'lll'
        age = 18
        def say(self):
            self.name ='xxx'
            self.age = 16
            print('my name is {0}'.format(self.name))
            print('my age is {0}'.format(self.age))
yyy = Student()
yyy.say()
"""         # 关于self

'''
class Teacher():
    name = 'yy'
    age = 18
    def say(self):
        self.name = 'yaoyao'
        self.age = 17
        print('My name is {0}'.format(self.name))
        #调用类的成员变量需要用__class__
        print('My age is {0}'.format(__class__.age))
    def sayAgain():
        print('My name is {0}'.format(__class__.name))
        print('My age is {0}'.format(__class__.age))
        print('Hello ,nice to see you again')

t =Teacher()
t.say()
Teacher.sayAgain()            
'''         # 调用绑定类函数使用类名

'''  
class A():
    name = 'li'
    age = 17
    def __init__(self):
        self.name = 'xin'
        self.age = 18
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name = 'yao'
    age = '19'

a = A()
#此时，系统会默认把a作为第一个参数传入函数
a.say()

#此时，self被a替换
A.say(a)
#同样可以把A作为参数传入
A.say(A())

#此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

#以上代码，利用鸭子模型
'''      # 关于self 的案例    鸭子类型

'''
class Person():
    # name是共有的成员
    name = 'lixinyao'
    # __age就是私有成员
    __age = 18
p = Person()
#name是公有变量
print(p.name)
#age是私有变量
#print(p.__age)         #试图打印这个私有变量会报错，显示没有这个属性

#name mangling技术
print(Person.__dict__)          #这样可以查看包括私有变量在内的所有变量
#可以发现，其实__age这个私有变量并不是隐藏了，而是改变了他的属性，改为了_Person__age
#然后发现通过_Person__age这个还是可以访问age的
print(p._Person__age)

'''         # 私有变量案例

'''  
#在python中，任何类都有一个共同的父类叫object
class person(object):
    name = None
    age = 18
    _score = 50 #这个是受保护的，子类可以用，不能公用
    __petname = 'yy'  #这个是私有的，仅自己可以用
    def sleep():
        print('sleeping ... ...')
#父类写在括号内
class teacher(person):
    teacher_id = '9527'
    name = 'xx'
    def make_test():                #为什么要删掉这里的self才可以在下面打印，             #有问题
        print('attention')
t=teacher
print(t.name)           #可以使用子类定义的变量        #父类里面定义了名字，子类里面也定义了名字，哪一个近就打印哪一个
print(teacher.name)      #还可以直接使用子类名称
print(t._score)         #子类可以使用父类的受保护的成员
#print(t.__petname)     #访问私有成员，则报错
print(t.teacher_id)      #子类可以定义独有的成员属性
t.sleep()                #自己的类中没有找到这个方法则继续往父类寻找
t.make_test()             #可以使用子类所定义的绑定类函数
'''       # 继承的语法

'''
class person():
    name = 'None'
    age = 18
    _score = 50 #这个是受保护的，子类可以用，不能公用
    __petname = 'yy'  #这个是私有的，仅自己可以用
    def sleep(self):
        print('sleeping ... ...')
    def work(self):
        print('make some money')
#父类写在括号内
class teacher(person):
    teacher_id = '9527'
    name = 'lll'
    def make_test(self):                #为什么要删掉这里的self才可以在下面打印，             #有问题
        print('attention')
    def work(self):
        #扩充父类的功能只需要调用父类相应的函数
        #person.work(self)
        #扩充父类的另一种方法，super代表得到父类
        super().work()      #调用父类里面的work方法
        self.make_test()    #self是本类
t = teacher()
t.work()
'''      # 子类扩充父类

'''
class animel():
    def __init__(self):
        print(animel)
class paxingani(animel):
    def __init__(self,name):
        print('paxingdongwu {0}'.format(name))
class dog(paxingani):
    def __init__(self):
        print('is dog')
d =dog()

class cat(paxingani):
    pass
#此时由于cat没有构造函数，则向上查找
#因为paxingani的构造函数需要两个参数（self，name），下面实例化的时候只给了一个，则报错，缺少一个参数
#c=cat()         #这里缺少参数   报错
'''         # 多继承

'''
class A():
    def __init__(self):
        print('A')
class B(A):
    def __init__(self):
        print('B')
class C(B):
    pass
#此时，首先查找C的构造函数
#如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止
c = C()

#参数不对应错误
# class A():
#     def __init__(self):
#         print('A')
# class B(A):
#     def __init__(self,name):
#         print('B')
#         print(name)
# class C(B):
#     pass
# c = C()
#C只有一个参数self，B则有self，name两个参数，参数不匹配，这段程序报错
'''
        # 扩展构造函数,直接调用
'''                                 
class A():
    def __init__(self):
        print('A')
class B(A):
    def __init__(self,name):
        print('B')
        print(name)
class C(B):
    #C中想扩展B的构造函数
    #即调用B的构造函数后再添加一些功能
    #有两种方法实现
    #第一种是通过父类名调用
    def __init__(self,name):
        #首先调用父类构造函数
        B.__init__(self,name)
        #再增加自己的功能
        print('这是C中附加的功能')
c = C ('这里是name')   #参数是一串字符，就是name，还有一个默认参数self

                                    # 扩展构造函数二 使用super
# class A():
#     def __init__(self):
#         print('A')
# class B(A):
#     def __init__(self,name):
#         print('B')
#         print(name)
# class C(B):
#     #第二种是使用super调用
#     def __init__(self,name):
#         super(C, self).__init__(name)
#         #再增加自己的功能
#         print('这是C中附加的功能')
# c = C ('这里是name')
#  '''        # 构造函数的调用


'''
class animel():
    def __init__(self):       #构造函数
        print(animel)
class paxingani(animel):
    def __init__(self):         
        print('paxingdongwu')
class dog(paxingani):
    #__init__就是构造函数
    #每次实例化的时候，第一个被自动调用
    #因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('is dog')
#实例化的时候，自动调用了dog的构造函数
#因为找到了构造函数，则不在查找父类的构造函数
kaka = dog()        #实例化会调用构造函数

#这里的cat没有写构造函数
class cat(paxingani):
    pass
#此时应该自动调用构造函数，应为cat没有构造函数，所以查找父类的构造函数
#在paxingani中查找到了构造函数，则停止向上查找构造函数
c = cat()
 '''        # 构造函数的概念

'''
# issubclass(
class A():
    pass
class B(A):
    pass
print(issubclass(B,A))  #检测B是不是A的子类

# isinstance(
class A():
    pass
a = A()
print(isinstance(a, A)) #检测a是不是A的实例

# hasattr(
class A():
    name = None
a = A()
print(hasattr(a,'name'))    #检测a实例中有没有‘name’这个属性
'''         # 类相关的函数

'''
#定义一个person类，具有name，age属性
#对于仍以输入的姓名，我们希望都用大写方式保存
#年龄，我们希望内部统一用整数保存
# x = property(fget, fset, fdel, doc)
class person():
    #函数名的名称可以随意
    def fget(self):
        return self._name * 2       #这个name读取两遍
    def fset(self,name):
        #upper 所有输入的姓名以大写形式保存
        self._name = name.upper()
    def fdel(self):
        self._name = 'NoName'
    #下面这些fget，fset，fdel是运行的顺序
    name = property(fget, fset, fdel,'对name进行以下操作')
p1 = person()       #实例化
p1.name = 'lll'       #对这个属性进行赋值
print(p1.name)       #打印这个类的类
 '''      # peroperty案例


'''
class A():
    name = 'no'
    age = 18
    def __getattr__(self, name):
        print('dddd')
        print(name)             #最后打印None是因为没有返回值
a = A()
print(a.age)
print(a.nam)
 '''        # 属性操作，getattr

'''
class A():
    def __init__(self,name=0):
        print('调用这个')
    def __call__(self):
        print('被调用2')
    def __str__(self):
        return '123 '
a = A()
print(a)
'''         # 操作类的函数

'''
#__getattr__
class A():
    name = 'me'
    age = 18
    def __getattr__(self, name):
        print('第一个被参数调用的属性')
        print(name)
        return '返回值'    #没有返回值则输出None
a = A()
print(a.name)
print(a.addr)           #__getattr__ 在调用实例的属性不存在时,自动调用__getattr__方法
'''        # 属性操作相关

'''
#__setattr__案例
class person():
    def __init__(self):
        self.BigName='小明'
    def __setattr__(self, name, value):
        print('设置属性:{0}'.format(name))
        #下面一句话会导致死循环
        #self.name=value
        #为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name,value)         #super是获取第一个类，也就是父类，这里直接当成父类使用
p = person()
# print(p.__dict__)
p.age = 18
'''         # 因为setattr造成的死循环

'''
#__gt__
class student():
    def __init__(self,name):
        self.name = name
    def __gt__(self,obj):
        print('{0}会比{1}大嘛？'.format(self,obj))
        return self._name > obj._name
stu1 = student('one')
stu2 = student('two')
print(stu1.__gt__)
print('stu1' > 'stu2')
'''         # 进行大于判断时候触发

'''
class person:
    #实例方法
    def eat(self):
        print(self)     #打印person的属性
        print('eating')
    #类方法
    #类方法第一个参数一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)      #打印属性
        print('playing')
    #静态方法
    #不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print('saying')
per = person()
#实例方法
per.eat()
#类方法
per.play()
person.play()
#静态方法
per.say()
person.say()
'''         # 类和对象的三种方法

'''
class A():
    def __init__(self):
        self.name='aaa'
        self.age=18
a =A()
#属性的三种用法
#1. 赋值
#2. 读取
#3. 删除
a.name = 'lxy'  #赋值
print(a.name)   #读取
del a.name  #删除
'''         # 属性的三种用法

'''
#类属性 property
#对应场景：
#对变量除了普通的三种操作，还想增加一些附加的操作，那么可以通过property完成
class A():
    def __init__(self):
        self.name = 'aaa'
        self.age = 18
    #此功能，是对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print('这是读取功能')
        return self.age
    #模拟的是对变量进行写操作的时候执行的功能
    def fset(self,name):
        print('这是写入功能')
        self.name = '图灵学院：'+name


    #fdel模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass
    #property的四个参数顺序是固定的
    #第一个参数代表读取的时候需要调用的函数
    #第二个参数代表写入的时候需要调用的函数
    #第三个是删除
    name2 = property(fget,fset,fdel,'这里是说明')
a = A()
print(a.name,a.age)
print(a.name2)
'''         # 类属性 property

'''
class animel():
    def sayhello(self):
        pass
class dog(animel):
    def sayhello(self):
        print('闻一下对方')
class person(animel):
    def sayhello(self):
        print('kiss me')
d = dog()
d.sayhello()

p = person()
p.sayhello()
'''         # 抽象

'''
#申明一个类并且指定当前类的元素
import abc
class human(metaclass=abc.ABCMeta):
    #定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass
    @abc.abstractstaticmethod
    def play():                     #上面都是抽象的方法
        pass
    def sleep(self):                #具体的方法
        print('sleeping....')
'''         # 抽象类的使用

'''
def sayhello(name):#函数名可以当变量使用

    print('{0}你好'.format(name))
sayhello('yy')          #调用这个函数使用
ll = sayhello           #这里把定义函数赋值给ll
ll('xx')                #ll就等于这个函数，并且可以当成这个函数来使用
'''         # 函数当变量使用

'''
#自己组装一个类
class A():
    pass
    def say(self):
        print('saying...  ...')
class B():
    def say(self):
        print('saying......')
A.say(9)
say=A.say     #把A类的say函数当作变量赋值给say

a = A()         #实例化a
a.say()         #这样子a就可以调用say函数了，说明函数可以当变量使用

b = B()         # 实例化b
b.say()         #b可以调用say函数
'''         # 自己组装一个类

'''
from types import MethodType        #从types导入出一个MethodType工具来进行绑定实例
class A():
    pass
def say(self):
    print('saying...  ...')
a = A()
#a.say =say         #可以绑定A()类，却不允许绑定a.say这个实例，如果一定要绑定这个实例可以借助别的工具
a.say = MethodType(say, A)         #用MethodType告诉系统把这个say当成方法使用，A是绑定在什么类上面
a.say()
'''         # 组装类例子 2,借用types.MethodType来直接绑定实例

'''
#先定义类应该具有的成员函数
def play(self):
    print('play games')
def swimming(self):
    print('go to swimming')
#利用type来创建一个类
#type(name,bases,dict)  name就是这个类的名字，bases是父类，dict是这个类拥有的属性（dict使用字典类型）
A = type('person',(object,),{'class_play':play,'class_swimming':swimming})  #'class_play':play  有一个方法，这个方法的功能是play
#然后就可以像访问正常类一样使用这个类
a = A()
a.class_play()          #这里就是调用这个方法了
a.class_swimming()
'''         # 利用type造一个类


# 元类写法是固定的，必须继承自type
# 元类一般命名以MetaClass结尾
class zzMetaClass(type):
    # 注意下面写法
    def __new__(cls, name, bases, attrs):
        print('这就是元类')
        attrs['serial'] = '123'
        attrs['addr'] = '江西电子信息'
        return type.__new__(cls, name, bases, attrs)
# 元类定义完就可以使用，使用注意写法
class Student(object,metaclass=zzMetaClass):      # 父类是object，把zzMetaClass用metaclass转给Student
    pass
t = Student()           # 这里调用的是zzMetaClass里面的内容
print(t.addr)
         # 元类演示
