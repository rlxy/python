
#直接调用文件模块
import p01
stu = p01.student('rr', 18)     #先给参数命名，p01文件模块里面的student类
stu.say()       #调用student类里面的内置函数say
p01.sayhallo()      #需要用到文件模块名调用外置函数，因为它不属于类里面，是属于文件模块里