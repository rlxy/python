import random
import time
import pygame

#屏幕大小常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新的帧率
FRAME_PER_SEC = 90
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#飞机发射子弹事件,因为上面把定时器常量给了敌机，所以+1 是为了不冲突
HERO_FIRE_EVENT = pygame.USEREVENT + 1




class GameSprites(pygame.sprite.Sprite):
    '飞机大战精灵'
    def __init__(self,image_name,speed=2,unspeed=1):

        #调用父类的初始化方法
        super().__init__()

        #定义对象属性
        self.image = pygame.image.load(image_name)  #image_name是图片的位置
        self.rect = self.image.get_rect() #获取图像的位置,对齐属性(top bottom left right)
        self.speed = speed
        self.unspeed = unspeed
    def update(self, *args):

        #在屏幕垂直方向上移动
        self.rect.y += self.speed

class BackGround(GameSprites):
    '游戏背景精灵'

    def __init__(self,is_alt=False):

        #1.调用父类实现精灵的创建(image/rect/speed)
        super().__init__('../image/background.png')

        #2.判断是否是交替图像，如果是，则需要设置初始化位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):

        #1.调用父类的方法实现
        super().update()
        #2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height :
            self.rect.y = -self.rect.height


class Enemy(GameSprites):
    '敌机精灵'
    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__('../image/enemy1.png')

        #2.指定敌机初始随机速度
        self.speed = random.randint(1,3)

        #3.指定敌机初始随机位置
        # self.rect.y = -43
        # self.rect.x = random.randint(0,423)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)


    def update(self):
        #1.调用父类方法，保持垂直方向的飞行
        super().update()
        #2.判断是否飞出屏幕，如果是就要删除敌机减少内存
        if self.rect.y >= SCREEN_RECT.height:
            print('敌机丢失，准备销毁')
            self.kill()
    def __del__(self):
        print('敌机销毁，销毁位置为：%s'% self.rect)


class Hero(GameSprites):
    '飞机精灵'
    def __init__(self):
        # 调用父类
        super().__init__('../image/me1.png',0)

        #设置飞机的初始位置 centerx 是x的中心点
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        #子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        #设置飞机移动
        self.rect.x += self.speed
        self.rect.y += self.unspeed
        if self.rect.x < 0 :
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width :
            self.rect.right = SCREEN_RECT.width
        elif self.rect.y < 0:
            self.rect.y = 0
            print(SCREEN_RECT.height)
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        print('子弹发射')
        #创建子弹精灵
        bullet = Bullet()
        #设置子弹精灵的位置    应该出现在飞机的正上方
        bullet.rect.bottom = self.rect.y - 10
        bullet.rect.centerx = self.rect.centerx

        #将精灵添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprites):
    #子弹精灵
    def __init__(self):
        super().__init__('../image/bullet1.png',-200)


    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print('子弹飞出屏幕，已失效')