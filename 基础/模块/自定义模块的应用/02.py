#借助于importlib包可以实现导入以数字开头的模块名称
import importlib
rr = importlib.import_module('01')      #因为模块名为数字不可取，所以把这个模块导入到‘rr’中
stu = rr.student()                      #这里就直接使用rr这个模块了
stu.say()
rr.sayhallo()