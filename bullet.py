# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:50:56 2018

@author: Administrator
"""

import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''
    def __init__(self,ai_settings,screen,ship,direction):
        '''飞船所在位置创建一个子弹对象'''
        super(Bullet,self).__init__()
        self.screen=screen
        #在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        if direction==0:
            self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.rect.x=ship.rect.centerx
            self.rect.top=ship.rect.top
        elif direction==1:
            self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.rect.x=ship.rect.centerx
            self.rect.bottom=ship.rect.bottom
        elif direction==2:
            self.rect=pygame.Rect(0,0,ai_settings.bullet_height,ai_settings.bullet_width)
            self.rect.y=ship.rect.centery
            self.rect.left=ship.rect.left
        elif direction==3:
            self.rect=pygame.Rect(0,0,ai_settings.bullet_height,ai_settings.bullet_width)
            self.rect.y=ship.rect.centery
            self.rect.right=ship.rect.right
        
        #self.rect.centerx=ship.rect.centerx
        #self.rect.top=ship.rect.top
        
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        self.direction=direction
    def update(self):
        if self.direction==0:
            self.y=self.y-self.speed_factor
        elif self.direction==1:
            self.y=self.y+self.speed_factor
        elif self.direction==2:
            self.x=self.x-self.speed_factor
        elif self.direction==3:
            self.x=self.x+self.speed_factor
        self.rect.y=self.y
        self.rect.x=self.x
    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)