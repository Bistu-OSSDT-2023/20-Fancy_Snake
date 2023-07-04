# -*- coding:utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import websocket
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
import pyaudio
from tkinter import *
import threading
import tkinter
import queue
from queue import Queue

from typing import List, Any
import pygame
import random
from sys import exit
from settings import Settings, Point
from score_board import Scoreboard
from heartboard import Lifeboard
from functions import *


# 贪吃蛇小游戏运行逻辑：

def snake_game(result_queue):
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
            clock.tick(1)
        elif(sp == 2):
            clock.tick(1)
    

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
       
        # 处理语音识别结果
        # 对贪吃蛇进行操作
        if not result_queue.empty():
            result = result_queue.get()
            print("识别结果: %s" % (result))
            if "左" in result or "佐" in result:
                if sets.snake1_direct == 'top' or sets.snake1_direct == 'bottom':
                    sets.snake1_direct = 'left'
            elif "右" in result or "又" in result or "6" in result:
                if sets.snake1_direct == 'top' or sets.snake1_direct == 'bottom':
                    sets.snake1_direct = 'right'
            elif "上" in result or "尚" in result:
                if sets.snake1_direct == 'left' or sets.snake1_direct == 'right':
                    sets.snake1_direct = 'top'
            elif "下" in result or "夏" in result:
                if sets.snake1_direct == 'left' or sets.snake1_direct == 'right':
                    sets.snake1_direct = 'bottom'

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



# 语音识别功能运行逻辑：

def voice_recognition(result_queue):

    STATUS_FIRST_FRAME = 0  # 第一帧的标识
    STATUS_CONTINUE_FRAME = 1  # 中间帧标识
    STATUS_LAST_FRAME = 2  # 最后一帧的标识

    # Ws_Param用于管理API的相应参数
    class Ws_Param(object):
        # 初始化
        # 设置API
        def __init__(self, APPID, APIKey, APISecret):
            self.APPID = APPID
            self.APIKey = APIKey
            self.APISecret = APISecret


            # 公共参数(common)
            self.CommonArgs = {"app_id": self.APPID}
            # 业务参数(business)，更多个性化参数可在官网查看
            self.BusinessArgs = {"domain": "iat", "language": "zh_cn", "accent": "mandarin", "vinfo":1,"vad_eos":10000}

        # 生成url
        def create_url(self):
            url = 'wss://ws-api.xfyun.cn/v2/iat'
            # 生成RFC1123格式的时间戳
            now = datetime.now()
            date = format_date_time(mktime(now.timetuple()))

            # 拼接字符串
            signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
            signature_origin += "date: " + date + "\n"
            signature_origin += "GET " + "/v2/iat " + "HTTP/1.1"
            # 进行hmac-sha256进行加密
            signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
            signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')

            authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
                self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
            authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
            # 将请求的鉴权参数组合为字典
            v = {
                "authorization": authorization,
                "date": date,
                "host": "ws-api.xfyun.cn"
            }
            # 拼接鉴权参数，生成url
            url = url + '?' + urlencode(v)
            # print("date: ",date)
            # print("v: ",v)
            # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
            # print('websocket url :', url)
            return url


    # 收到websocket消息的处理
    # 定义了一个on_message函数，用于处理接收到的WebSocket消息
    # 函数中解析了返回的JSON数据，获取到code、sid、data等信息
    # 如果返回的code不为0，则打印错误信息。如果code为0，则从data中提取结果，并将结果显示在界面上
    def on_message(ws, message):
        try:
            code = json.loads(message)["code"]
            sid = json.loads(message)["sid"]
            if code != 0:
                errMsg = json.loads(message)["message"]
                print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))

            else:
                data = json.loads(message)["data"]["result"]["ws"]
                result = ""
                for i in data:
                    for w in i["cw"]:
                        result += w["w"]

                if result == '。' or result=='.。' or result==' .。' or result==' 。':
                    pass
                else:
                    t.insert(END, result)
                    result_queue.put(result)
                    print("翻译结果: %s" % (result))

        except Exception as e:
            print("receive msg,but parse exception:", e)


    # 收到websocket错误的处理
    def on_error(ws, error):
        print("### error:", error)


    # 收到websocket关闭的处理
    def on_close(ws):
        pass
        # print("### closed ###")


    # 收到websocket连接建立的处理
    # on_open函数内部创建了一个新的线程，并在该线程中进行录音和发送语音数据的操作
    # 录音部分利用pyaudio库对声音进行采样，然后将采样到的声音通过WebSocket发送给服务器
    def on_open(ws):
        def run(*args):
            status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧
            CHUNK = 520                 # 定义数据流块
            FORMAT = pyaudio.paInt16  # 16bit编码格式
            CHANNELS = 1  # 单声道
            RATE = 16000  # 16000采样频率
            p = pyaudio.PyAudio()
            # 创建音频流
            stream = p.open(format=FORMAT,  # 音频流wav格式
                            channels=CHANNELS,  # 单声道
                            rate=RATE,  # 采样率16000
                            input=True,
                            frames_per_buffer=CHUNK)

            print("- - - - - - - Start Recording ...- - - - - - - ")

            for i in range(0,int(RATE/CHUNK*60)):
                buf = stream.read(CHUNK)
                if not buf:
                    status = STATUS_LAST_FRAME
                if status == STATUS_FIRST_FRAME:

                    d = {"common": wsParam.CommonArgs,
                        "business": wsParam.BusinessArgs,
                        "data": {"status": 0, "format": "audio/L16;rate=16000",
                                "audio": str(base64.b64encode(buf), 'utf-8'),
                                "encoding": "raw"}}
                    d = json.dumps(d)
                    ws.send(d)
                    status = STATUS_CONTINUE_FRAME
                    # 中间帧处理
                elif status == STATUS_CONTINUE_FRAME:
                    d = {"data": {"status": 1, "format": "audio/L16;rate=16000",
                                "audio": str(base64.b64encode(buf), 'utf-8'),
                                "encoding": "raw"}}
                    ws.send(json.dumps(d))

                # 最后一帧处理
                elif status == STATUS_LAST_FRAME:
                    d = {"data": {"status": 2, "format": "audio/L16;rate=16000",
                                "audio": str(base64.b64encode(buf), 'utf-8'),
                                "encoding": "raw"}}
                    ws.send(json.dumps(d))
                    time.sleep(1)
                    break

            stream.stop_stream()
            stream.close()
            p.terminate()
            ws.close()
        thread.start_new_thread(run,())

    # 启动WebSocket，并将之前定义的各个回调函数指定为WebSocketApp的回调函数
    def run():
        global wsParam
        wsParam = Ws_Param(APPID='53c6a120', APIKey='13149579cb2d458ca55841671d67cdec',
                        APISecret='NDU4ZTgwODBmNDFkZmI1YmJiMmQ2NDVm')
        websocket.enableTrace(False)
        wsUrl = wsParam.create_url()
        ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)
        ws.on_open = on_open
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}, ping_timeout=2)

    # 在程序的入口处创建了一个Tkinter窗口，并在窗口中添加了一个文本框和一个按钮。按钮点击时会启动一个新的线程来执行run函数

    #def thread_it(func, *args):
        #t = threading.Thread(target=func, args=args)
        #t.setDaemon(True)
        #t.start()

    root = Tk()
    t = Text(root)
    t.pack()

    #tkinter.Button(root, text='go', command=lambda :thread_it(run,)).pack()
    #root.mainloop()

    run()


# 总程序运行逻辑：多线程执行

result_queue = Queue()  # 创建共享队列

# 创建贪吃蛇小游戏线程
snake_thread = threading.Thread(target=snake_game, args=(result_queue,))

# 创建语音识别线程
voice_thread = threading.Thread(target=voice_recognition, args=(result_queue,))

# 将贪吃蛇小游戏线程设置为守护线程，确保主线程退出时自动结束
snake_thread.daemon = True

# 启动线程
voice_thread.start()
snake_thread.start()



