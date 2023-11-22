#os  -操作系统相关
import os

#getcwd 获取当前的工作目录
mrdir = os.getcwd()
print('当前目录为：{0}'.format(mrdir))

# chdir() 改变当前的目录
os.chdir('/新建文件夹/高级-包/模块')
mrdir = os.getcwd()
print('当前目录为：{0}'.format(mrdir))

#listdir()  获取一个目录中所有子目录和文件的名称列表            os.list(path)
ld = os.listdir()
print(ld)

# makedirs()   在当前目录递归创建文件夹         没有返回值

# rst = os.makedirs('yaoyao')
# print(rst)

#system() 运行系统shell命令       os.system(系统命令)
# rst = os.system('ls')

#getenv() 获取指定的系统环境变量值      os.getenv(环境变量名)
#相应的还有putenv()      和getgnv相反

#exit() 退出当前程序
# print(exit())


#值部分
# os.curdir: curretn dir,当前目录
# os.pardir: parent dir, 父目录
# os.sep:当前系统的路径分隔符
# os.linesep:当前系统的换行符号
# os.name:当前系统名称
print('当前系统名称:{0}'.format(os.name))

import os.path as op
# os.path 模块

# abspath() 将路径转化为绝对路径
#abselute 绝对
absp = op.abspath('.')
print(absp)

#basename() 获取路径中的文件名部分
file = op.basename('/新建文件夹/高级-包/模块')
print(file)

#os.path.dirname(path):返回path中的文件夹部分，结果不包含'\'
dn = op.dirname('/新建文件夹/高级-包/模块')
print('dirname :{0}'.format(dn))

#join() 将多个路径拼合成一个路径
bn = '/新建文件夹/高级-包'
fn = '模块'
p = op.join(bn,fn)
print('拼合成的路径：{0}'.format(p))


# os.path.getmtime(path):文件或文件夹的最后  修改  时间，从新纪元到访问时的秒数。
# os.path.getatime(path):文件或文件夹的最后  访问  时间，从新纪元到访问时的秒数。
# os.path.getctime(path):文件或文件夹的  创建  时间，从新纪元到访问时的秒数。
m = op.getmtime('E:\新建文件夹\高级-包\模块')
a = op.getatime('E:\新建文件夹\高级-包\模块')
c = op.getctime('E:\新建文件夹\高级-包\模块')
print('文件修改时间：{0}'.format(m))
print('文件访问时间：{0}'.format(a))
print('文件创建时间：{0}'.format(c))

# os.path.getsize(path):文件或文件夹的大小，若是文件夹返回0。
size = op.getsize('E:\新建文件夹\高级-包\模块\常用模块.md')
print('文件大小:{0}'.format(size))

#os.path.exists(path):文件或文件夹是否存在，返回True 或 False。
exist = op.exists('E:\新建文件夹\高级-包\模块')
print(exist)

print(os.sep)           #文件分隔号 //
print(os.extsep)        #当前目录表示 .
print(os.pathsep)       #
print(os.linesep)       #回车



###在路径的相关操作中，不要手动拼写地址，因为手动拼写的路径并不能具有移植性，比如按window系统里面的方法得到的文件到Linux系统里面会没用
###所以路径操作中建议使用os 模块





