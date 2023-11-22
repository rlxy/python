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


pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()


# 游戏循环
i = 0
while True:

    #tick方法指定频率
    clock.tick(60)      #每秒刷新屏幕多少下

    i += 1
    print(i)
    pass

pygame.quit()