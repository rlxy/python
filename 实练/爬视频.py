from urllib import parse        #url解析库 做编码的
import tkinter.messagebox as msgbox     #tk  如果出现错误 错误会返回一个信息
import tkinter as tk    #tkinter 制作软件的库
import webbrowser   #控制浏览器
import re   #正则表达式

'''
使用面向对象的思维编写今天的脚本
两个编程方式
    函数时编程
    基于类的编程
'''

class App :
    #首先的u走法是给这个类自定义一些属性
    '''
    构造函数 魔术方法
    可以给这个类自定义属性
    重写
    '''
    def __init__(self,width = 500,height = 300):
        self.w = width
        self.h = height

        self.title = 'vip视频破解助手'
        self.root = tk.Tk(className=self.title)

        #vip视频播放地址 定义变量类型
        self.url = tk.StringVar()

        #定义选择哪一个播放源
        self.v = tk.IntVar()

        #默认为1
        self.v.set(1)

        #Frame 空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        #控件内容设置
        group = tk.Label(frame_1,text = '暂时只有一个视频播放通道：',padx = 10 ,pady = 10)
        tb = tk.Radiobutton(frame_1,text = '唯一通道',variable = self.v,value = 1,width = 10,height = 3)

        label = tk.Label(frame_2,text = '请输入视频链接：')
        #输入框
        entry = tk.Entry(frame_2,textvariable = self.url,highlightcolor = 'Fuchsia',highlightthickness = 1,width = 35)
        play = tk.Button(frame_2,text = '播放',font = ('楷体',12),fg = 'purple',width = 2,height = 1,command = 's')

        #控件布局 将这些控件显示再你的软件上
        frame_1.pack()
        frame_2.pack()

        #确定控件的位置    row 行  column  列
        group.grid(row = 0 , column = 0)
        tb.grid(row = 0,column = 1)

        label.grid(row = 0,column = 0)
        entry.grid(row = 0,column = 1)

        #播放按钮的位置确认以及风格设置
        play.grid(row = 1,coumn = 3)

    #声明一个函数 实现播放功能
    def video_play(self):
        #视频解析的网站地址
        port = 'http://www.wmxz.wang/video.php?url= '

        #使用正则表达式 去判断用户输入的网站是否合法
        if re.match(r'^https?:/{2}\w,+$',self.url.get()):
            #拿到用户输入的值并且存到变量中
            ip = self.url.get()

            #做域名编码
            ip = parse.quote_plus(ip)

            #用浏览器打开网址
            webbrowser.open(port+ip)
        else:
            msgbox.showerror(title='错误',message='视频地址无效，请重新输入！')

    def loop(self):
        self.root.resizable(True,True)
        self.root.mainloop()

if __name__ == '__main__':
    app = App
    app.loop()



























