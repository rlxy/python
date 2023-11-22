"""
时间：2022.10.23
"""
import pygame
import random

# 变量
W = 800
H = 600
ROW = 40
COL = 30
food_W = W / 20
food_H = H / 20
res_size = 20
bg_color = (40, 40, 60)
line_color = (0, 0, 0)
line_width = 1
# 游戏频率
fre = 10
# 蛇身
snakes = []
score = 0

class Point:
    """
    网格具体位置
    row：行
    col：列
    """
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def snake_copy(self):
        """
        为了吃到食物增加蛇长度
        """
        return Point(row=self.row, col=self.col)

# row第几行，col第几列
head = Point(row=int(ROW / 2), col=int(COL / 2))
print(head.row, head.col)
snake_color = (100, 100, 100)

x = random.randint(0, int(food_H) - 1)
y = random.randint(0, int(food_W) - 1)
food = Point(row=x, col=y)
food_color = (200, 200, 200)

def food_eat():
    """
    食物
    """
    pos = Point(row=(random.randint(0, int(food_H) - 1)), col=(random.randint(0, int(food_W) - 1)))
    eat_food = False
    if head.row == pos.row and head.col == pos.col:
        eat_food = True

    if not eat_food:
        return pos

def rec(point, color):
    """
    网格
    """
    # 尺寸 res_size
    cell_width = H/COL
    cell_hight = W/ROW
    # 位置
    left = point.col*cell_width
    right = point.row*cell_hight
    # 网格横线
    for x in range(20, 600, 20):
        pygame.draw.line(bg, line_color, (0, x), (800, x))
    # 网格竖线
    for y in range(20, 800, 20):
        pygame.draw.line(bg, line_color, (y, 0), (y, 600))
    pygame.draw.rect(bg, color, ((left, right), (cell_width, cell_hight)))

def monitor():
    """
    监听函数
    """
    global init_direct
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
            print('开始监听')
        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741906 or event.key == 119:
                if init_direct == 'left' or init_direct == 'right':
                    init_direct = 'up'
            elif event.key == 1073741905 or event.key == 115:
                if init_direct == 'left' or init_direct == 'right':
                    init_direct = 'down'
            elif event.key == 1073741904 or event.key == 97:
                if init_direct == 'up' or init_direct == 'down':
                    init_direct = 'left'
            elif event.key == 1073741903 or event.key == 100:
                if init_direct == 'up' or init_direct == 'down':
                    init_direct = 'right'
    if init_direct == 'left':
        head.col -= 1
    elif init_direct == 'right':
        head.col += 1
    elif init_direct == 'up':
        head.row -= 1
    elif init_direct == 'down':
        head.row += 1
    # 判断是否死亡
    if head.col < 0 or head.col > 40:
        state = False
        print('game over，碰到墙壁')
    elif head.row < 0 or head.row > 30:
        state = False
        print('game over，碰到墙壁')
    for snake in snakes:
        if snake.row == head.row and snake.col == head.col:
            state = False
            print("吃到自己了")

def judge(snake_row, snake_col, food_row, food_col):
    """
    判定吃到食物
    """
    if snake_row == food_row:
        if snake_col == food_col:
            return True

if __name__ == '__main__':
    pygame.init()
    # (宽，高)
    bg = pygame.display.set_mode((W, H))
    pygame.display.set_caption("贪吃蛇")
    bg.fill(bg_color)
    clock = pygame.time.Clock()

    # 缺失补偿:由于吃第一个食物没有增加长度
    snakes.insert(0, head.snake_copy())
    state = True
    init_direct = 'left'
    while state:
        monitor()
        print(init_direct)
        print('蛇头位置', head.row, head.col)
        print('食物位置', food.row, food.col)

        # 吃到食物则从小刷新食物位置
        eat = False
        if head.row == food.row and head.col == food.col:
            print('--------------------------')
            eat = True
            food = food_eat()
            score += 10
        snakes.insert(0, head.snake_copy())
        # print(snakes)
        if not eat:
            snakes.pop()
        pygame.draw.rect(bg, bg_color, ((0, 0), (W, H)))
        rec(head, snake_color)
        for snake in snakes:
            rec(snake, snake_color)
        rec(food, food_color)
        pygame.display.flip()
        clock.tick(fre)
        if not state:
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("最终得分：{}，蛇总长为{}".format(score, len(snakes)))
                        exit()
"""
添加积分
添加结束页面
"""