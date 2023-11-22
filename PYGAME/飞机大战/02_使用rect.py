import pygame

# 游戏中所有可见元素都是以一个矩形来描述其位置的，描述一个矩形的位置需要  x,y,width,height
# Rect是pygame专门提供的一个用于描述矩形的类
# 注意 Rect并不需要调用pygame.init()方法
hero_rect = pygame.Rect(100, 500, 120, 125)

print('x=%d,y=%d'% (hero_rect.x,hero_rect.y))
print('width=%d,height=%d'%(hero_rect.width, hero_rect.height))
print('size=%d %d'% hero_rect.size)

