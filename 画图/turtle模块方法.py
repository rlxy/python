'''
'''
import turtle as t

# 海龟(turtle)
# forward(distance):海龟，默认海龟向右移动
t.forward(100)
# left(angle):向左转
t.left(90)
# right(angle):向右转
t.right(90)
# position():获取海龟当前坐标
t.position()
# reset():清空画布，海龟重置位置
t.reset()
# clear():清空画布，海龟位置不变
t.clear()
# backward():后退，不会改变海龟的朝向
t.backward(1)
# up():停止作画（抬起画笔），
t.up()
# t.down():开始作画（放下画笔）   up和down之间的轨迹不显示
t.down()

# t.pensize(width):改变画笔宽度
t.pensize(3)
# t.hideturtle():隐藏海龟
t.hideturtle()
# t.setheading(to_angle):让海龟朝指定方向；-角度为正-->逆时针旋转;-角度为负-->顺时针旋转
t.setheading(90)
# t.pencolor(color):画笔颜色
t.pencolor('color')
# t.write(str,font=('字体','字体大小')):让海龟写字，
t.write('text')

t.mainloop()

