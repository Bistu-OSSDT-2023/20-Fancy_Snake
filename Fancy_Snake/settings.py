# 存储一些初始设置参数
from tkinter import SEL
import pygame
from functions import *

class Settings():
	
	def __init__(self):

		self.quit = True
		self.quit1 = True
		self.quit2 = True

		self.width = 800
		self.hight = 600

		# ROW和col是将整个屏幕分块，整个屏幕共有多少个行块和多少列块
		self.ROW = 40
		self.COL = 60

		# snake 头颜色可以自定义
		self.head1_color = (0, 0, 153)
		self.head2_color = (200, 0, 0)
		# 身体的颜色
		self.snake1_color = (0, 204, 255)
		self.snake2_color = (255, 204, 0)
		# 食物颜色
		self.snake1Food_color = (255, 120, 0)
		self.speedup_food_color = (204,0,204)
		self.speeddown_food_color = (96,96,96)
		self.big_food_color = (0,255,0)
		
		# snake的移动速度
		self.s1_speed = 1
		self.s2_speed = 1
		
		self.init_s1()
		self.init_s2()
		# 食物坐标
		#self.snake1Food = gen_food(self)
	

	def init_s1(self):
		self.snake1_direct = 'left'
		# 蛇头坐标定在中间
		self.head1 = Point(row=int(self.ROW/2 -10), col=int(self.COL/2))
		# 初始化蛇身的元素数量
		self.snake1 = [
			Point(row=self.head1.row, col=self.head1.col + 1),
			Point(row=self.head1.row, col=self.head1.col + 2),
			Point(row=self.head1.row, col=self.head1.col + 3)
			]
		# 对玩家1的剩余生命值进行计算：
		self.life1 = 1


	def init_s2(self):
		self.snake2_direct = 'left'
		self.head2 = Point(row=int(self.ROW/2 +10), col=int(self.COL/2))
		self.snake2 = [Point(row=self.head2.row, col=self.head2.col + 1),
			Point(row=self.head2.row, col=self.head2.col + 2),
			Point(row=self.head2.row, col=self.head2.col + 3)
			]
		# 对玩家2的剩余生命值进行计算：
		self.life2 = 1

		
		
