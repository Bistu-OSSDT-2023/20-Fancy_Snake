import random
from turtle import position
import pygame

# 设置一个initial模块，让self.snake撞墙后是重置到初始位置

# 定义坐标类：
class Point():
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(row=self.row, col=self.col)


# 生成食物方法：（不让食物生成在蛇的身体里面）
def gen_food(sets):
    while 1:
        position = Point(row=random.randint(0, sets.ROW - 1), col=random.randint(0, sets.COL - 1)) # 生成一个随机方块点
        is_coll = False
        if sets.head1.row == position.row and sets.head1.col == position.col: # 如果随机生成的方块点与头重合，则退出
            is_coll = True
        for body in sets.snake1:
            if body.row == position.row and body.col == position.col:
                is_coll = True
                break
        if not is_coll:
            break
    return position

# 需要执行很多步画图操作 所以定义一个坐标点画图函数，对Point对象进行绘制
def rects(window, sets, point, color):
    # 定位所画点的坐标位置，因而需要left和top
    left = point.col * sets.width / sets.COL
    top = point.row * sets.hight / sets.ROW
    # 将方块涂色
    pygame.draw.rect(window, color, (left, top, sets.width / sets.COL, sets.hight / sets.ROW)) # (视窗，颜色，涂色大小)

# 定义一个坐标点画图函数，将Point对象绘制为圆形
def draw_circle(window, sets, point, color):
    # 计算圆心的坐标
    center_x = point.col * sets.width / sets.COL + sets.width / sets.COL / 2
    center_y = point.row * sets.hight / sets.ROW + sets.hight / sets.ROW / 2
    # 计算圆的半径
    radius = min(sets.width / sets.COL, sets.hight / sets.ROW) / 2
    # 绘制圆形
    pygame.draw.circle(window, color, (int(center_x), int(center_y)), int(radius))

# 检测事件响应
def check_events(sets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sets.quit = False

		# 检测是否按下鼠标
		#   elif event.type == pygame.MOUSEBUTTONDOWN:
		#	mouse_x, mouse_y = pygame.mouse.get_pos()

		# 检测键盘是否按下
		elif event.type == pygame.KEYDOWN:
			check_keydown(sets, event)

# 检测按键按下
def check_keydown(sets, event):
	# 对第一条蛇进行设置：
	if event.key == pygame.K_w: # 当想要向上移动时，只有当目前的方向是左右是才执行
		# sets.snake1_direct 默认为 'top'
		if sets.snake1_direct == 'left' or sets.snake1_direct == 'right':
			sets.snake1_direct = 'top'
	if event.key == pygame.K_s:
		if sets.snake1_direct == 'left' or sets.snake1_direct == 'right':
			sets.snake1_direct = 'bottom'
	if event.key == pygame.K_a:
		if sets.snake1_direct == 'top' or sets.snake1_direct == 'bottom':
			sets.snake1_direct = 'left'
	if event.key == pygame.K_d:
		if sets.snake1_direct == 'top' or sets.snake1_direct == 'bottom':
			sets.snake1_direct = 'right'

	# 对第二条蛇进行设置：
	if event.key == pygame.K_UP: # 当想要向上移动时，只有当目前的方向是左右是才执行
		# sets.snake2_direct 默认为 'top'
		if sets.snake2_direct == 'left' or sets.snake2_direct == 'right':
			sets.snake2_direct = 'top'
	if event.key == pygame.K_DOWN:
		if sets.snake2_direct == 'left' or sets.snake2_direct == 'right':
			sets.snake2_direct = 'bottom'
	if event.key == pygame.K_LEFT:
		if sets.snake2_direct == 'top' or sets.snake2_direct == 'bottom':
			sets.snake2_direct = 'left'
	if event.key == pygame.K_RIGHT:
		if sets.snake2_direct == 'top' or sets.snake2_direct == 'bottom':
			sets.snake2_direct = 'right'

	# 这里小细节,蛇不可以直接左右上下 要判断当前是在什么状态下前行