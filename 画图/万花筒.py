from turtle import *
import time
a =130
b = 360     #万花筒的所有角度加起来是360
pu()
goto(0, 0)
pd()
while True:
    color('#B088FF')
    forward(100)
    right(a)
    b -= (180-a)
    begin_fill()
    if b == 0:
        break
time.sleep(5)
