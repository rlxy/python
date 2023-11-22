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
#3，update 更新屏幕显示
pygame.display.update()

#绘制飞机图像
#png格式支持透明的，透明区域（就是那灰和白小格子区域）不会显示任何内容并且不会遮挡住其他内容
hero = pygame.image.load('./image/me1.png')
screen.blit(hero,(200,500))
pygame.display.update()



#游戏循环
while True:
    pass

pygame.quit()