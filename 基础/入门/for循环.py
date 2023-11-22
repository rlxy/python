"""
Filename: ./
Author: 药药
Contact: 1579954422@qq.com
introduce：for循环演示
"""

stu_list = ['lxy', 'zyx', 'nux', 'dxx']
for stu in stu_list:        # 循环一遍上面的sut_list
    if stu == 'lxy':           # 循环遇见lxy则输出下面的
        print('this is me')
    elif stu == 'zyx':               # 循环到zyx则循环下面的
        print('this is zyx，is my love')
    else:               # 否则遇见别的就输出下面的
        print('stranger')
print('must to be happy')
