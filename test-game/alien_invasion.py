import pygame
from pygame.sprite import Group

from button import Button
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并建一个屏幕对象
    pygame.init()
    i_settings = Settings()
    screen = pygame.display.set_mode(size=(i_settings.screen_width, i_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(i_settings, screen)
    # 创建一个统计信息的实例
    stats = GameStats(i_settings)
    # 创建一艘飞船
    ship = Ship(i_settings, screen)
    # 创建一个储存子弹的数组
    bullets = Group()
    # 创建外星人数组
    aliens = Group()
    gf.create_fleet(i_settings, screen, ship, aliens)

    # 创建分数
    sb = Scoreboard(i_settings, screen, stats)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(i_settings, screen, play_button, sb, stats, ship, aliens, bullets)
        if stats.game_active:
            # 更新飞船
            ship.update()
            # 更新子弹列,并调用每个子弹的update()方法
            bullets.update()
            # 更新外星人
            gf.update_aliens(i_settings, aliens)
            # 超出屏幕删除子弹
            gf.delete_bullet(bullets)
            # 子弹与外星人碰撞
            gf.aliens_bullets_to_hit(i_settings, screen,stats, sb, ship, aliens, bullets)
            # 验证飞船碰撞
            gf.check_ship_hit(i_settings, screen, play_button, sb, stats, ship, aliens, bullets)
            # 外星人到底部
            gf.check_aliens_bottom(i_settings, screen, play_button, sb, stats, ship, aliens, bullets)
            # 重新绘制屏幕
            gf.update_screen(i_settings, screen, play_button, sb, stats, ship, bullets, aliens)
        else:
            gf.update_screen(i_settings, screen, play_button, sb, stats, ship, bullets, aliens)


run_game()
