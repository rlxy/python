import pygame

#pygame初始化
pygame.init()

#创建主窗口 需要窗口大小：800*1000
screen = pygame.display.set_mode((480,700))

#绘制背景图像
#加载图像数据
bg = pygame.image.load('./image/background.png')
#blit 绘制图像
screen.blit(bg,(0,0))

#绘制飞机图像
hero = pygame.image.load('./image/me1.png')
screen.blit(hero,(150,300))


pygame.display.update()


#创建时钟对象
clock = pygame.time.Clock()

#1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

#游戏循环
while True:
    #tick方法指定频率
    clock.tick(60)

    #捕获事件
    event_list = pygame.event.get()     #游戏运行时所在窗口内做的所有操作都会以一个list形式打印出来
    if len(event_list) > 0 :
        print(event_list)

    #2.修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700

    #3.调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    #4.调用update方法更新显示
    pygame.display.update()

    pass

pygame.quit()