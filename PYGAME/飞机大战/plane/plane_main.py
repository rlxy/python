import random

import pygame

from plane_sprites import *

DEL_ENEMY = 0

class PlaneGame(object):
    def __init__(self):
        print('游戏初始化')
        #1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建游戏时钟
        self.clock = pygame.time.Clock()
        #3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        #4.设置定时器事件 -创建敌机  1000毫秒 = 1秒
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,1000)


    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(is_alt=True)
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

        #创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        #创建友方飞机精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print('游戏开始....')

        while True:

            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 2.事件监听
            self.__event_handler()

            # 3.碰撞检测
            self.__check_collide()

            # 4.更新/绘制精灵组
            self.__update_sprites()

            # 5.更新显示
            pygame.display.update()
            pass

    def __event_handler(self):

        for event in pygame.event.get():
            #判断是否退出游戏
            if event.type == pygame.QUIT :
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print('敌机号....')
                #创建敌机精灵
                enemy = Enemy()
                #将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            if event.type == HERO_FIRE_EVENT:
            # fire_key_pressed = pygame.key.get_pressed()
            # if fire_key_pressed[pygame.K_SPACE]:
                self.hero.fire()



            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print('向右移动')
            '''
            上面是第一种捕获按键的方式，只有抬起按键才算一次按键事件，操作灵活性大大下降
            下面是第二种捕获按键的方式，按住方向键不放，就能够实现持续出现按键事件，操作灵活性才高
            '''
        #使用键盘提供的方法获取键盘按键 -获取按键元组
        keys_pressed = pygame.key.get_pressed()
        #判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_UP]:
            self.hero.unspeed = -2
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.unspeed = 2
        else:
            self.hero.speed = 0
            self.hero.unspeed = 0

    def __check_collide(self):
        #子弹摧毁敌机
        global DEL_ENEMY
        bullet_enemy = pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        if len(bullet_enemy) > 0 :
            DEL_ENEMY += 1

        #敌机撞毁飞机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏结束')
        print('本次击毁敌机',DEL_ENEMY)

        pygame.quit()
        exit()




if __name__ == '__main__':
    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.start_game()


