# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:44:38 2018

@author: Administrator
"""
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    '''初始化飞船并设置其初始位置'''
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen=screen
    #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        
        #将飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #储存飞船属性的浮点值
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.bottom)
        
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    def updata(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left>0:
            self.centerx-=self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top>0:
            self.centery-=self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centery+=self.ai_settings.ship_speed_factor
            
        #更新对象
        self.rect.centerx=self.centerx
        self.rect.bottom=self.centery
    
    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.centerx=self.screen_rect.centerx
        self.centery=self.screen_rect.bottom