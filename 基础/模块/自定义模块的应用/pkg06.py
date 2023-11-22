from pkg02 import *         #导入pkg02这个包里面的所有内容

stu = p01.student()         #因为__init__里面用__all__导入了p01
stu.say()                    #直接执行p01里面的say（）

#  ininit()     这里我想导入__init__里面的ininit()函数，可是因为init里面已经有了all来导入的模块，不考虑除了all导入模块以外的内容