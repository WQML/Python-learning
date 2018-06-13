# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:37:47 2018

@author: Administrator
"""
import pygame.font
class Buttom():
    def __init__(self,ai_settings,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        
        #设置按钮的尺寸和其他属性
        self.width,self.height=200,50
        self.buttom_color=(0,0,250)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48,bold=True,italic=True)
        
        #创建按钮的rect对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        
        #按钮的标签只需要创建一次
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        '''将msg渲染成图像，并使其在按钮上居中'''
        self.msg_image=self.font.render(msg,True,self.text_color,self.buttom_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.buttom_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)