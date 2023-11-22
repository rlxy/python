#五角星的总角度数是180
import turtle
import time
i = 0
while i < 6 :
    turtle.forward(100)     #向当前画笔方向移动100像素长度
    turtle.right(144)       #顺时针移动144°
    i +=1
time.sleep(10)
