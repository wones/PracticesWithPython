import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



#初始化游戏并创建一个屏幕对象
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button=Button(ai_settings,screen,"Play")


    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #创建飞船
    ship=Ship(ai_settings,screen)
    bg_color=(ai_settings.bg_color)
    bullets=Group()
    aliens=Group()
    alien=Alien(ai_settings,screen)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()


