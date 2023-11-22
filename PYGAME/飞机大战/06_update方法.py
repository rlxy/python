import pygame

#pygame初始化
pygame.init()

#创建主窗口 需要窗口大小：800*1000
screen = pygame.display.set_mode((480,700))

#绘制背景图像
#1,加载图像数据
bg = pygame.image.load('./image/background.png')
#2，blit 绘制图像
screen.blit(bg,(0,0))

#绘制飞机图像
hero = pygame.image.load('./image/me1.png')
screen.blit(hero,(200,500))



#可以在screen对象完成所有的blit方法之后统一调用一次display.update方法，这样就不用每次绘制图片都调用一次了
pygame.display.update()     #上面代码全部完成统一调用update更新图像


#游戏循环
while True:
    pass

pygame.quit()