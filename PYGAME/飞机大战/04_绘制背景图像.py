import pygame

#pygame初始化
pygame.init()

#创建主窗口 需要窗口大小：800*1000
screen = pygame.display.set_mode((480,700))

#绘制背景图像
#1,加载图像数据
bg = pygame.image.load('./image/background.png')    #参数：ImageFile_path
#2，blit 绘制图像
screen.blit(bg,(0,0))                               #参数，图像,(位置)
#3，update 更新屏幕显示
pygame.display.update()


#游戏循环
while True:
    pass

pygame.quit()