#sys  系统特定的参数和功能
#该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数，他始终可用
import sys

print(sys.argv[0])          #命令行参数列表，第一个元素是程序本身路径

print(sys.path)             #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值

print('python解释程序的版本信息',sys.version)          #获取python解释程序的版本信息

print('操作系统平台名称',sys.platform)         #返回操作系统平台名称

print('取最大递归层数',sys.getrecursionlimit())  #获取最大递归层数

print('解释器默认编码',sys.getdefaultencoding())     #获取解释器默认编码

print('内存数据存到文件里的默认编码：',sys.getfilesystemencoding())     #获取内存数据存到文件里的默认编码

print('最大int值：',sys.maxsize)        #  最大的int值python2中是 maxint

# sys.exit('程序退出')   #里面的参数会在退出程序前打印，，sys.exit()用于在主线程退出，os._exit()用于在线程中退出

print('标准输入',sys.stdin.readline())         #标准输入  需要在控制台输入

print('标准输出：',sys.stdout.write('python\n'))         #标准输出，，还会返回字符串长度

print()



print(sys.byteorder)