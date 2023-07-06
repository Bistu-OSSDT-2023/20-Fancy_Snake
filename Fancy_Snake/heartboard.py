import pygame.font

class Lifeboard():

    def __init__(self, sets, window):


        self.window = window
        self.window_rect = window.get_rect()
        
        self.text_color1 = (0, 200, 255)
        self.text_color2 = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 30)
        
        self.prep_life(sets)
    
    def prep_life(self, sets):

        # ��snake��setting������life1��ֵ�ļ��㷽�������ص�����
        life1_str = "Life: {}".format(sets.life1)
        # ��������ֵ��ȾΪͼ��
        self.life1_image = self.font.render(life1_str, True, self.text_color1, (230, 255, 230))
        # ����ͼ����Ƶ�λ��
        self.life1_rect = self.life1_image.get_rect()
        self.life1_rect.left = 10
        self.life1_rect.bottom = sets.hight - 7
        
        # ��life1������ͬ��
        life2_str = "Life: {}".format(sets.life2)
        self.life2_image = self.font.render(life2_str, True, self.text_color2, (230, 255, 230))
        self.life2_rect = self.life2_image.get_rect()
        self.life2_rect.right = sets.width - 10
        self.life2_rect.bottom = sets.hight - 7
    
    def show_life(self):
        self.window.blit(self.life1_image, self.life1_rect)
        self.window.blit(self.life2_image, self.life2_rect)