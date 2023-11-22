import pygame

class GameSprites(pygame.sprite.Sprite):
    '飞机大战精灵'
    def __init__(self,image_name,speed=1):

        #调用父类的初始化方法
        super().__init__()

        #定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):

        #在屏幕垂直方向上移动
        self.rect.y += self.speed