import pygame

pygame.init()

#创建主窗口 需要窗口大小：800*1000
screen = pygame.display.set_mode((480,700))
'''
参数：(resolution=(0,0),flags=0,depth=0)  默认都是0
resolution:指定窗口的宽和高，默认创建的窗口和屏幕大小一致
flags:参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
depth:参数表示颜色的粒数，默认自动匹配
'''

#游戏循环
while True:
    pass

pygame.quit()