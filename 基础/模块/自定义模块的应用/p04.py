from p01 import student,sayhallo
stu = student('yaoyao')
stu.say()
sayhallo()


from p01 import *       #这里是把p01里面的所有都导入   *代表所有
stu = student('yaoyao')         #类赋值给stu并加参数
stu.say()                       #调用stu下面的say函数
sayhallo()                      #直接调用了sayhallo模块

