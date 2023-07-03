from typing import List, Any

import pygame
import random
from sys import exit
from settings import Settings, Point
from score_board import Scoreboard
from heartboard import Lifeboard
from functions import *

sets = Settings()

# 初始化，屏幕宽度和高度
pygame.init()
window = pygame.display.set_mode((sets.width, sets.hight))
pygame.display.set_caption('Multiplay Greedy Snake_qxd')


score = Scoreboard(sets,window)
Life = Lifeboard(sets,window)

sfoods = []
for i in range(4): # 食物的数量
    sfoods.append(gen_food(sets))

speedup_food = gen_food(sets)
speeddown_food = gen_food(sets)
big_food = gen_food(sets)

# 设置帧频率
clock = pygame.time.Clock()

# 设置速度控制变量
sp = 1

# 设置速度食物出现变量
speed_food_appear = True
cot = 0

# 设置big食物出现变量
big_food_appear = True
cot2 = 0

while sets.quit:
    # 处理帧频 锁帧
    if(sp == 1):
        clock.tick(10)
    elif(sp == 2):
        clock.tick(20)
    
    # 设置该项可以改变游戏速度，值越大速度越快
    
    check_events(sets)
                    
    # 吃普通食物 （当头目前的位置和食物的坐标相同时）
    snake1_eat = False
    snake2_eat = False
    for index, food in enumerate(sfoods):
        if (sets.head1.row == food.row and sets.head1.col == food.col):
            snake1_eat = True
            sfoods[index] = Point(row=random.randint(0, sets.ROW - 1), col=random.randint(0, sets.COL - 1))
        if (sets.head2.row == food.row and sets.head2.col == food.col):
            snake2_eat = True
            sfoods[index] = Point(row=random.randint(0, sets.ROW - 1), col=random.randint(0, sets.COL - 1))

    # 吃速度食物
    cot += 1

    if (sets.head1.row == speedup_food.row and sets.head1.col == speedup_food.col):
        sp = 2
        # 使当前速度食物消失
        speed_food_appear = False
    if (sets.head2.row == speedup_food.row and sets.head2.col == speedup_food.col):
        sp = 2
        speed_food_appear = False

    if (sets.head1.row == speeddown_food.row and sets.head1.col == speeddown_food.col):
        sp = 1
        speed_food_appear = False
    if (sets.head2.row == speeddown_food.row and sets.head2.col == speeddown_food.col):
        sp = 1
        speed_food_appear = False

    # 吃big食物
    cot2 += 1

    if (sets.head1.row == big_food.row and sets.head1.col == big_food.col and big_food_appear == True):
        big_food_appear = False
        s1increase_array = [sets.snake1[len(sets.snake1) - 3], sets.snake1[len(sets.snake1) - 2],
                            sets.snake1[len(sets.snake1) - 1]]
        sets.snake1.extend(s1increase_array)  # 长度加3

    if(sets.head1.row == big_food.row-1 and sets.head1.col == big_food.col and big_food_appear == True):
        big_food_appear = False
        s1increase_array = [sets.snake1[len(sets.snake1)-3],sets.snake1[len(sets.snake1)-2],sets.snake1[len(sets.snake1)-1]]
        sets.snake1.extend(s1increase_array)  # 长度加3

    if (sets.head1.row == big_food.row +1 and sets.head1.col == big_food.col and big_food_appear == True):
        big_food_appear = False
        s1increase_array = [sets.snake1[len(sets.snake1) - 3], sets.snake1[len(sets.snake1) - 2],
                                sets.snake1[len(sets.snake1) - 1]]
        sets.snake1.extend(s1increase_array)  # 长度加3

    if (sets.head1.row == big_food.row  and sets.head1.col == big_food.col-1 and big_food_appear == True):
        big_food_appear = False
        s1increase_array = [sets.snake1[len(sets.snake1) - 3], sets.snake1[len(sets.snake1) - 2],
                            sets.snake1[len(sets.snake1) - 1]]
        sets.snake1.extend(s1increase_array)  # 长度加3

    if (sets.head1.row == big_food.row  and sets.head1.col == big_food.col+1 and big_food_appear == True):
        big_food_appear = False
        s1increase_array = [sets.snake1[len(sets.snake1) - 3], sets.snake1[len(sets.snake1) - 2],
                                sets.snake1[len(sets.snake1) - 1]]
        sets.snake1.extend(s1increase_array)  # 长度加3

    if (sets.head2.row == big_food.row and sets.head2.col == big_food.col and big_food_appear == True):
        big_food_appear = False
        s2increase_array = [sets.snake2[len(sets.snake1) - 3], sets.snake2[len(sets.snake2) - 2],sets.snake2[len(sets.snake2) - 1]]
        sets.snake2.extend(s2increase_array)

    if (sets.head2.row == big_food.row-1 and sets.head2.col == big_food.col and big_food_appear == True):
        big_food_appear = False
        s2increase_array = [sets.snake2[len(sets.snake1) - 3], sets.snake2[len(sets.snake2) - 2],
                                sets.snake2[len(sets.snake2) - 1]]
        sets.snake2.extend(s2increase_array)

    if (sets.head2.row == big_food.row +1 and sets.head2.col == big_food.col and big_food_appear == True):
        big_food_appear = False
        s2increase_array = [sets.snake2[len(sets.snake1) - 3], sets.snake2[len(sets.snake2) - 2],
                                    sets.snake2[len(sets.snake2) - 1]]
        sets.snake2.extend(s2increase_array)

    if (sets.head2.row == big_food.row and sets.head2.col == big_food.col-1 and big_food_appear == True):
        big_food_appear = False
        s2increase_array = [sets.snake2[len(sets.snake1) - 3], sets.snake2[len(sets.snake2) - 2],
                        sets.snake2[len(sets.snake2) - 1]]
        sets.snake2.extend(s2increase_array)

    if (sets.head2.row == big_food.row and sets.head2.col == big_food.col+1 and big_food_appear == True):
        big_food_appear = False
        s2increase_array = [sets.snake2[len(sets.snake1) - 3], sets.snake2[len(sets.snake2) - 2],
                                sets.snake2[len(sets.snake2) - 1]]
        sets.snake2.extend(s2increase_array)


    # 使速度食物每隔一定时间刷新一次
    if (cot%300 == 0):
        speedup_food = gen_food(sets)
        speeddown_food = gen_food(sets)
        speed_food_appear = True

    # 使big食物每隔一定时间刷新一次
    if (cot2%400 == 0):
        big_food = gen_food(sets)
        big_food_appear = True

    # 处理蛇的身子    # 1.把原来的头插入到sets.snake1的头上    # 2.把最后一个sets.snake1删掉

    sets.snake1.insert(0, sets.head1.copy()) # 每一次从头部增加了一个块，所以当没有吃东西的时候，需要每次删除掉一个模块来抵消，否则就会是拖尾的效果
    if not snake1_eat: # 没有吃东西的时候
        sets.snake1.pop() # 必须pop掉末尾的模块
    
    sets.snake2.insert(0, sets.head2.copy())
    if not snake2_eat:
        sets.snake2.pop()

    # sets.snake 1 移动一下
    if sets.snake1_direct == 'left':
        sets.head1.col -= sets.s1_speed
    if sets.snake1_direct == 'right':
        sets.head1.col += sets.s1_speed
    if sets.snake1_direct == 'top':
        sets.head1.row -= sets.s1_speed
    if sets.snake1_direct == 'bottom':
        sets.head1.row += sets.s1_speed
        
    if sets.snake2_direct == 'left':
        sets.head2.col -= sets.s2_speed
    if sets.snake2_direct == 'right':
        sets.head2.col += sets.s2_speed
    if sets.snake2_direct == 'top':
        sets.head2.row -= sets.s2_speed
    if sets.snake2_direct == 'bottom':
        sets.head2.row += sets.s2_speed 
        
    # 判断s1身体是否撞到边缘或撞到自身
    s1dead = False
    if sets.head1.col < 0 or sets.head1.row < 0 or sets.head1.col >= sets.COL or sets.head1.row >= sets.ROW:
        s1dead = True
    for body in sets.snake1: # s1头部碰撞到s1身体
        if sets.head1.col == body.col and sets.head1.row == body.row:
            s1dead = True
            break
    for body in sets.snake2: # s1头部碰撞到s2身体
        if sets.head1.col == body.col and sets.head1.row == body.row:
            s1dead = True
            break
    if s1dead:
        sets.init_s1()
        s1dead = False
        sets.life1 -= 1
        if(sets.life1 == 0):
            # sets.head1.row, sets.head1.col = int(sets.ROW/2 -10), int(sets.COL/2) # 重新设定蛇的身体和位置
            # sets.snake1 = []
            print('Game Over! Player2 win!')
            sets.quit = False

    
    # 判断s2身体是否撞到边缘或撞到自身
    s2dead = False
    if sets.head2.col < 0 or sets.head2.row < 0 or sets.head2.col >= sets.COL or sets.head2.row >= sets.ROW:
        s2dead = True
    for body in sets.snake2:
        if sets.head2.col == body.col and sets.head2.row == body.row:
            s2dead = True
            break
    for body in sets.snake1:
        if sets.head2.col == body.col and sets.head2.row == body.row:
            s2dead = True
            break
    if s2dead:
        sets.init_s2()
        s2dead = False
        sets.life2 -= 1
        if(sets.life2 == 0):
            # sets.head2.row, sets.head2.col = int(sets.ROW/2 -10), int(sets.COL/2)
            # sets.snake2 = []
            print('Game Over! Player1 win!')
            sets.quit = False


    # 判断s1与s2是否头部相撞：
    s1dead = False
    s2dead = False
    if(sets.head1.col == sets.head2.col and sets.head1.row == sets.head2.row):
        s1dead = True
        s2dead = True
    if s1dead and s2dead:
        sets.head1.row, sets.head1.col = int(sets.ROW/2 -10), int(sets.COL/2)
        sets.snake1 = []
        sets.head2.row, sets.head2.col = int(sets.ROW/2 -10), int(sets.COL/2)
        sets.snake2 = []
        print('Game Over! No Winner!')
        sets.quit = False

        
    # 背景画图
    pygame.draw.rect(window, (230, 255, 230), (0, 0, sets.width, sets.hight))

    # 蛇头
    rects(window, sets, sets.head1, sets.head1_color)
    rects(window, sets, sets.head2, sets.head2_color)
    # 绘制食物
    for food in sfoods:
        draw_circle(window, sets, food, sets.snake1Food_color)
    # 绘制速度食物
    if(speed_food_appear):
        rects(window, sets, speedup_food, sets.speedup_food_color)
        rects(window, sets, speeddown_food, sets.speeddown_food_color)

    # 绘制big食物
    if(big_food_appear):
        rects(window, sets, big_food, sets.big_food_color)
        rects(window, sets, Point(big_food.row - 1, big_food.col), sets.big_food_color)
        rects(window, sets, Point(big_food.row, big_food.col - 1), sets.big_food_color)
        rects(window, sets, Point(big_food.row + 1, big_food.col), sets.big_food_color)
        rects(window, sets, Point(big_food.row, big_food.col + 1), sets.big_food_color)

    # 绘制蛇的身子
    for body1 in sets.snake1:
        rects(window, sets, body1, sets.snake1_color)
    for body2 in sets.snake2:
	    rects(window, sets, body2, sets.snake2_color)
    # 绘制得分
    score.prep_score(sets)
    score.show_score()
    
    Life.prep_life(sets)
    Life.show_life()

    # 交还控制权
    pygame.display.flip()



    # 调整游戏速度的小道具设计：
    # 设置全局变量sp = 1（默认值为1）
    # 在while循环里，当sp = 1，帧率为10帧
    # 在while循环里，当sp = 2，帧率为20帧（加速）
    # 设置特殊食物两种，一种加速食物，一种减速食物；
    # 当在while循环中，检测是否有蛇吃到加速食物：吃到的话sp = 2
    # 当在while循环中，检测是否有蛇吃到减速食物：吃到的话sp = 1
    # 关键：加速食物和减速食物的出现机制：每隔30s出现一次


    # 增加蛇的长度的“营养食物”设计：
    # 设计一个“营养食物”，使得蛇吃掉这个食物后，能够将其身体长度增加多段

    # 替换食物的贴图，使得食物更加精致

    # 为了避免用户同时按两个按键使蛇立即死亡，必须加以判断用户的输入



    # 设计UI界面，使得游戏能够点击“Start”开始，并且在玩家死后可以有“ReStart”选项使游戏重新进行



    # 进阶：
    # 接入AI对战模型，实现人机对战
    # 接入语音识别与语言文字处理AI大模型，实现语音控制蛇的走向




