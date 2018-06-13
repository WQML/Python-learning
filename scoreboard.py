# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:38:49 2018

@author: Administrator
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship 
class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        self.screen=screen
        self.ai_settings=ai_settings
        self.stats=stats
        self.screen_rect=screen.get_rect()
        
        #显示得分信息是使用的字体
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,38)
        
        #准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        '''将得分渲染成图片'''
        rounded_score=int(round(self.stats.score,-1))#精确位数，如果为负数就整点，-1表示整十近似
        score_str='{:,}'.format(rounded_score)#格式化显示数字，这里就是用','作为千位间隔
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        
        #将得分信息显示在右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
        
    def prep_high_score(self):
        high_score=int(round(self.stats.high_score,-1))
        high_score_str='{:,}'.format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #将最高分信息显示在顶部中央
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top
    def prep_level(self):
        self.level_image=self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        #将等级放在得分下方
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10
    def prep_ships(self):
        '''显示还剩下多少飞船数目'''
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_settings,self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
    
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
        

