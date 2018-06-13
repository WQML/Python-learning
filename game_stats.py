# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:08:00 2018

@author: Administrator
"""

class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False
        with open('score.txt','r+') as file_object:
            self.score_save=file_object.read()
            if(self.score_save==''):
                self.high_score=0
            else:
                try:
                    self.high_score=int(float(self.score_save))#如果被恶意随意修改就不给初始化
                except ValueError:
                    self.high_score=0
                    pass
    def reset_stats(self):
        '''初始化游戏期间可能变化的统计信息'''
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
            