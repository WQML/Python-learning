# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:59:54 2018

@author: Administrator
"""
from bullet import Bullet
from time import sleep
import sys
import pygame
from alien import Alien
def check_keydown_events(event,ai_settings,screen,ship,bullets,stats):
    '''响应按键'''
    if event.key==pygame.K_d:
        ship.moving_right=True
    elif event.key==pygame.K_a:
        ship.moving_left=True
    elif event.key==pygame.K_w:
        ship.moving_up=True
    elif event.key==pygame.K_s:
        ship.moving_down=True
    elif event.key==pygame.K_UP:
        fire_bullet(ai_settings,screen,ship,bullets,0)
    elif event.key==pygame.K_DOWN:
        fire_bullet(ai_settings,screen,ship,bullets,1)
    elif event.key==pygame.K_LEFT:
        fire_bullet(ai_settings,screen,ship,bullets,2)
    elif event.key==pygame.K_RIGHT:
        fire_bullet(ai_settings,screen,ship,bullets,3)
    elif event.key==pygame.K_ESCAPE:
        save_high_score(stats)
        sys.exit()
    elif event.key==pygame.K_SPACE and stats.game_active:
        ai_settings.pause*=-1
        

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        '''隐藏光标'''
        ai_settings.initialize_dynamic_settings()
        ship.center_ship()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        

def check_keyup_events(event,ai_settings,screen,ship,bullets):
    '''响应松开'''
    if event.key==pygame.K_d:
        ship.moving_right=False
    elif event.key==pygame.K_a:
        ship.moving_left=False
    elif event.key==pygame.K_w:
        ship.moving_up=False
    elif event.key==pygame.K_s:
        ship.moving_down=False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#结束的时候除了离开，还需要看情况是否保存最高分
            save_high_score(stats)
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets,stats)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
            
            
def check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collision=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collision:
        for aliens in collision.values():
            stats.score+=ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level+=1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)            
            
def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人编队'''
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_num_alien_x(ai_settings,alien.rect.width)
    num_rows=get_numbers_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(num_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)  
            
def check_fleet_edges(ai_settings,aliens):
    '''如果外星人位于屏幕边缘，就采取相应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
        
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

         
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien) 
    
def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    '''检查是否有外星人到达屏幕底端'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break 

def check_high_score(stats,sb):
    '''检查是否诞生了新的最高分'''
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
          
def fire_bullet(ai_settings,screen,ship,bullets,direction):
    if len(bullets)<ai_settings.bullet_allowed:
        new_bullet=Bullet(ai_settings,screen,ship,direction)
        bullets.add(new_bullet)            
            
def get_num_alien_x(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_numbers_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可以容纳多少行的外星人'''
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    '''影响被外星人撞到的飞船'''
    if stats.ships_left>0:
        #将剩余飞船数目减一
        stats.ships_left-=1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(1)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
        
def updata_screen(ai_setting,screen,stats,sb,ship,aliens,bullets,play_button):
    '''更新屏幕并切换到新屏幕'''
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    
def updata_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    screen_rect=screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0 or bullet.rect.bottom>screen_rect.bottom or bullet.rect.left<0 or bullet.rect.right>screen_rect.right:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets)
    
def updata_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)
    
def save_high_score(stats):
    with open('score.txt') as file_object:#打开保存最高分的文件
        score_temp=file_object.read()#读取文件
    if(score_temp!=''):#如果文件不是空
        try:
            high_score0=int(float(score_temp))#获取文件中的最高分
        except ValueError:
            high_score0=0
    else:
        high_score0=0
    if stats.high_score>high_score0:
        with open('score.txt','w') as file_object:
            file_object.write(str(stats.high_score))


        

    


    