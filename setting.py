# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:33:12 2018

@author: Administrator
"""

class Setting():
    '''储存外星人入侵的所有设置的类'''
    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(230,230,230)
        #飞船设置
        self.ship_limit=3
        #子弹设置 
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=3
        #外星人设置
        self.fleet_drop_speed=10
        #加快速度节奏设置
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        self.pause=-1
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.0
        self.bullet_speed_factor=1.5
        self.alien_speed_factor=1
        self.fleet_direction=1#1表示右移，-1表示左移
        self.alien_points=50
        
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        
