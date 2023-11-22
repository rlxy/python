import openpyxl
import json

class Excel:
    def __init__(self,path:str,infor:list):
        self.path = path
        self.infor = infor
        self.list = []
        self.dict = []
    def excel_file(self,sheet:str,title):
        workbook = openpyxl.load_workbook(self.path) #excel表的path
        sheet = workbook[sheet]     #指定具体sheet表
        for index,row in enumerate(sheet.rows):
            excel_list = []
            excel_dict = {}
            #判断是否有表头
            if index == 0 :     #循环到第一行做出判断，是否有表头
                if title :  #title为运行时填的参数，参数为 False 判断为无表头，不跳过继续运行，如果为True 判断为有表头直接跳过
                    continue
            for row_index,row_value in enumerate(row):

                #格式化日期
                if row_index == 3 : #循环到第四行就把第四行的时间格式化
                    date = row_value.value.strftime('%Y-%m-%d')
                    excel_list.append(date)
                    excel_dict[self.infor[row_index]] = date
                else:
                    excel_list.append(row_value.value)
                    excel_dict[self.infor[row_index]] = row_value.value
            self.list.append(excel_list)
            self.dict.append(excel_dict)

if __name__ == '__main__':
    path = './数据.xlsx'
    infor = ['son', 'name', 'gender', 'birthday', 'mobile', 'email', 'address']
    E = Excel(path,infor)
    E.excel_file('Sheet1',False)    #sheet,,判断有无表头
    print(E.list)
    print(E.dict)