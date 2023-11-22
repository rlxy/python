import os
import json

class DI:
    def __init__(self,path:str,infor:list):
        self.path = path
        self.infor = infor
        self.json_list = []
        self.json_dict = []
    def read_json_file(self):
        # s使用open函数读取文件
         with open(self.path, 'r', encoding='utf-8') as f:
            f = json.load(f)
            for i in f['objects'] :
                self.json_list.append(list(i.values()))
            # print(self.json_list)       #双重列表
            for i in self.json_list:
                dict = {}
                for index,value in enumerate(self.infor) :
                    dict[value] = i[index]

                    self.json_dict.append(dict)

            print(self.json_dict)   #字典列表


if __name__ == '__main__':
    path = os.getcwd() + '/数据.json'
    infor = ['son','name','gender','birthday','mobile','email','address']
    D = DI(path,infor)
    D.read_json_file()
