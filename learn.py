# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:41:41 2018

@author: Administrator
"""
import pygame
from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Buttom
from scoreboard import Scoreboard
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Setting()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button=Buttom(ai_settings,screen,'Play')
    ship=Ship(ai_settings,screen)
        
    #开始游戏的主循环
    bullets=Group()
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.updata()
            gf.updata_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.updata_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.updata_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
