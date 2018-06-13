# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:09:14 2018

@author: Administrator
"""

import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    '''表示单个外星人的类'''
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        
        #加载外星人的图像并设置属性
        self.image=pygame.image.load('alien.bmp')
        self.rect=self.image.get_rect()
        
        #每个外星人初始都在品目左上角附近
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #储存外星人的准确位置
        self.x=float(self.rect.x)
    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)
    def update(self):
        '''向右移动外星人'''
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)#逐次向右移动,速度在setting中控制
        self.rect.x=self.x
        
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
            