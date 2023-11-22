#调用p01并改名字为p，而后直接使用p调用
import p01 as p
stu = p.student('aa',18)    #赋值给stu并给参数
stu.say()               #用stu调用类下面的函数
p.sayhallo()            #用p调用sayhallo函数
