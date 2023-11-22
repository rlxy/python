#   shutil模块
#主要作用与拷贝文件用的
import shutil
import os

#copy()  复制文件
#copy2() 复制文件，保留源数据（文件信息）
#注意：copy和copy2的唯一区别在于copy复制文件时尽量保留源数据
# rst = shutil.copy('来源的路径','目标路径')

#copyfile（）将一个文件中的内容复制到另外一个文件当中
# rst = shutil.copyfile('源路径','目标路径')

#move（） 移动文件/文件夹
#rst = shutil.move('源路径'，'目标路径')


#shutil.copyfileobj(文件1，文件2)：将文件1的数据覆盖copy给文件2。
'''
f1 = open("文件1",encoding="编码形式")            #encoding 是编码
f2 = open("文件2","w",encoding="编码形式")        #'w' 是write写入
shutil.copyfileobj(f1,f2)
'''

#shutil.copymode(文件1，文件2)：之拷贝权限，内容组，用户，均不变。
'''
def copymode(src,dst):
    """copy mode bits from src to dst"""
    if hasattr(os,'chmod'):
        st = os.stat(stc)
        mode = stat.S_IMODE(st.st_mode)
        os.chmod(dst,mode)
'''

#shutil.copystat(文件1，文件)：只拷贝了权限

# shutil.copy2(文件1，文件2)：拷贝了文件和状态信息。

# shutil.copytree(源目录，目标目录)：可以递归copy多个目录到指定目录下。

# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ignore=None)
# 递归的去拷贝文件

# 例如：copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

# shutil.rmtree(目标目录)：可以递归删除目录下的目录及文件。

# shutil.move(源文件，指定路径)：递归移动一个文件。

# shutil.make_archive()：可以压缩，打包文件。



#归档和压缩   make_archive()

#归档：把多个文件或者文件夹合并到一个文件当中
# rst = shutil.make_archive('归档后的路径文件','后缀','需要归档的路径文件')      这里的后缀只有 eg zip or tar

#unpack_archive() 解包操作
#shutil.unpack_archive('归档文件地址'，'解包之后的地址')


##压缩：用算法吧多个文件或者文件夹无损或者有损压缩合并到一个文件当中
#shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的
# zipfile 压缩解压
# 压缩
# import zipfile
# z = zipfile.ZipFile('压缩包')        创建一个压缩包
# zf = z.getinfo('压缩包中的文件')
# print(zf)   打印那个压缩包的详细信息

#zipfile.namelist()
#获取zip文件中的所有文件名称
# nl = zf.namelist()
# print(nl)

#zipfile.extractall(path[,member,[pwd]])
#解压zip文档中的所有文件到当前目录。参数members的默认值为zip文档内的所有文件名称列表
# rst = zf.extractall('path')
# print(rst)








