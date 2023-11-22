import pygame
import random

class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

pygame.init()

speed = 5
H = 800
W = 600
COL = 80   # 每个格子的大小 = （H/COL） * (W/ROW)
ROW = 60
size = (H, W)
window = pygame.display.set_mode(size)
pygame.display.set_caption('title')

background_color = (255, 255, 255)

head = Point(row=int(ROW/2), col=int(COL/2))
head_color = (0, 128, 128)
food = Point(row=random.randint(0, COL-1), col=random.randint(0, ROW-1))
food_color = (255, 255, 0)

init_direct = 'left'            # 方向：left-1，right+1，up-1，down+1

def rec(point, color):
    cell_width = W/ROW   # 宽度
    cell_height = H/COL   # 高度

    left = point.col*cell_height
    # print(left)
    top = point.row * cell_width
    # print(top)
    pygame.draw.rect(window, color, ((left, top), (cell_width, cell_height)))


clock = pygame.time.Clock()



# #产出食物
# def Pfood():
#     while 1 :




Quit = True
while Quit:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            Quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741906 or event.key == 119:
                init_direct = 'up'
            elif event.key == 1073741905 or event.key == 115:
                init_direct = 'down'
            elif event.key == 1073741904 or event.key == 97:
                init_direct = 'left'
            elif event.key == 1073741903 or event.key == 100:
                init_direct = 'right'

    eat_food = (head.row == food.row and head.col == food.col)



    if init_direct == 'left':
        head.col -= 1
    elif init_direct == 'right':
        head.col += 1
    elif init_direct == 'up':
        head.row -= 1
    elif init_direct == 'down':
        head.row += 1

    # 渲染
    pygame.draw.rect(window, background_color, (0, 0, H, W))

    rec(head, head_color)
    rec(food, food_color)


    pygame.display.flip()


    clock.tick(10)
