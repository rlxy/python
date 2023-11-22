'''
读取文本文件使用open函数，有三个方法读取：
1) read() ---把整个文件一次读取到str
2）readlines --- 把整个文件一次读取到list集合，一行是一个元素
3) readline ---一次读取一行，处理完后 再读取下一行
'''
import os

class DI:
    #构造函数
    def __init__(self,path:str,infos:list):
        self.path = path
        self.infos = infos
        self.di_list = []
        self.di_dict = []

    def read_txt_file(self):
        '''读取文本文件、csv文件'''
        #异常处理
        try:
            #s使用open函数读取文件
            with open(self.path,'r',encoding='utf-8') as f:
                #读取第一行
                one_line = f.readline()
                #while判断是否为空
                while one_line:
                    #文本
                    one_line_list = one_line.replace(' ','').strip().split(',')
                    self.di_list.append(one_line_list)

                    #定义字典集合
                    dict = {}
                    for index,value in enumerate(self.infos):
                        dict[value] = one_line_list[index]  #index 是enumerate函数的索引
                    self.di_dict.append(dict)     #把所有dict字典组成一个list
                    one_line = f.readline()

        except Exception as e :
            raise e

if __name__ == '__main__':
    path = os.getcwd() + '\数据.txt'  #txt文件路径

    infos = ['sno','name','gender','birthday','mobile','email','address']


    read_txt = DI(path,infos)
    try:
        read_txt.read_txt_file()

        # di_list
        print('双重列表')
        print(read_txt.di_list)
        # for i in read_txt.di_list:
        #     print(i)

        print('--'*50)

        # di_dict
        print('字典列表：')
        print(read_txt.di_dict)
        # for i in read_txt.di_dict:
        #     print(i)


    except Exception as a:
        print('问题原因：' + str(a))










