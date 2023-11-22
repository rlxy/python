"""
Filename: Tkinter.py
Author: 药药
Contact: 1579954422@qq.com
introduce： 讲解tkinter库内常用函数并使用
"""
# 测试tkinter包是否好用
# import tkinter      #导入库
# tkinter._test()       #一个普通的图形界面

# hello world
# base = tkinter.Tk()
# 消息循环
# base.mainloop()

"""
#Label的例子
import tkinter
base = tkinter.Tk()
#负责标题
base.wm_title('Label Test')
lb = tkinter.Label(base,text='Python Label')        #base指定副组件的位置，后面text是属性设置
#给相应组件指定布局
lb.pack()   #布局设置

lb1 = tkinter.Label(base,text= "Python AI")
lb1.pack()

lb2 = tkinter.Label(base,text= "这个背景是绿色", background = 'green')
lb2.pack()

lb3 = tkinter.Label(base,text= "这个背景是蓝色", background = 'blue')
lb3.pack()

base.mainloop()
"""

'''
###Button 案例
import tkinter

def showLabel():
    global baseFrame
    #在函数中定义一个label
    #label的辅组件是baseFrame
    lb = tkinter.Label(baseFrame,text = '显示Label')
    lb.pack()
baseFrame = tkinter.Tk()
#生成一个按钮
#command参数指示，当按钮被按下的时候，执行哪个函数
btn = tkinter.Button(baseFrame,text='Show Label',command=showLabel)
btn.pack()
baseFrame.mainloop()
'''

'''
#pack布局案例
import tkinter

baseFrame = tkinter.Tk()
#以下所有代码都是创建一个组件，然后布局

btn1 = tkinter.Button(baseFrame,text = 'A')
btn1.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.Y)
#靠左   是扩展   填充Y方向
btn2 = tkinter.Button(baseFrame,text = 'B')
btn2.pack(side=tkinter.TOP,expand=tkinter.YES,fill=tkinter.BOTH)
#靠上扩展XY方向全部填充
btn2 = tkinter.Button(baseFrame,text = 'C')
btn2.pack(side=tkinter.RIGHT,expand=tkinter.YES,fill=tkinter.NONE,anchor=tkinter.NE)
#靠右扩展不填充 放在东北
btn2 = tkinter.Button(baseFrame,text = 'D')
btn2.pack(side=tkinter.LEFT,expand=tkinter.NO,fill=tkinter.Y)
#靠左不扩展Y方向填充
btn2 = tkinter.Button(baseFrame,text = 'E')
btn2.pack(side=tkinter.TOP,expand=tkinter.NO,fill=tkinter.BOTH)
#靠上不扩展XY方向全部填充
btn2 = tkinter.Button(baseFrame,text = 'F')
btn2.pack(side=tkinter.BOTTOM,expand=tkinter.YES)
#靠下扩展
btn2 = tkinter.Button(baseFrame,text = 'G')
btn2.pack(anchor=tkinter.SE)
#放在SE东南方向
baseFrame.mainloop()
'''


# grid 布局案例
'''
import tkinter
baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame,text='账号：').grid(row=0,sticky=tkinter.W)
tkinter.Entry(baseFrame).grid(row=0,column=1,sticky=tkinter.E)  #Entry是输入框  row是行，column是列

lb2 = tkinter.Label(baseFrame,text='密码').grid(row=1,sticky=tkinter.W)
tkinter.Entry(baseFrame).grid(row=1,column=1,sticky=tkinter.E)

brn = tkinter.Button(baseFrame,text='登陆').grid(row=2,column=1,sticky=tkinter.W)

baseFrame.mainloop()
'''


# 消息机制
'''
import tkinter

def baseLabel(event):
    global baseFrame
    lb = tkinter.Label(baseFrame,text = '点击成功')
    lb.pack()

#画出程序总框架
baseFrame = tkinter.Tk()

lb = tkinter.Label(baseFrame,text = '按钮')
#label绑定相应的消息和处理函数
#自动获取左键点击，并启动相应的狐狸函数baseLabel
lb.bind('<Button-1>',baseLabel)
lb.pack()

#启动消息循环
#到此，表示程序开始运行
baseFrame.mainloop()
'''


# 一个普通的菜单实例
'''
import tkinter
baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)
for item in ['File','Edit','View','About'] :
    menubar.add_command(label = item)
baseFrame['menu'] = menubar
baseFrame.mainloop()
'''

# 级联菜单
'''
import tkinter
baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)
emenu = tkinter.Menu(menubar)
file = tkinter.Menu(menubar)
file.add_command(label = 'settings')
for item in ["Copy","Past",'Cut'] :
    emenu.add_command(label=item)

menubar.add_cascade(label='File',menu=file)
menubar.add_cascade(label='Edit',menu=emenu)
menubar.add_cascade(label = 'About')
baseFrame['menu'] = menubar
baseFrame.mainloop()
'''


# 简单画布

import tkinter
baseFrame = tkinter.Tk()

cvs = tkinter.Canvas(baseFrame, width=300, height=200)
cvs.pack()
# 一条线需要两个点指明起始   开始的xy  和结束的xy
# 参数数字的单位是px
cvs.create_line(23, 23, 190, 234)
cvs.create_text(56, 67, text='i love python')

baseFrame.mainloop()
