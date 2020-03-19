import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien


def compare_high_score(stats, sb):
    if stats.old_high_score > stats.high_score:
        sb.write_file_high_score()
    else:
        sb.write_file_high_score()


def check_events(i_settings, screen, play_button, sb, stats, ship, aliens, bullets):
    """事件监听核心函数"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            compare_high_score(stats, sb)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, i_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 返回单击鼠标坐标的元组
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(i_settings, screen, sb, stats, ship, aliens, bullets, play_button, mouse_x, mouse_y)


def check_key_down_events(event, i_settings, screen, ship, bullets):
    """按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(i_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, ship):
    """松开事件"""
    # 控制左右按键标记
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(i_settings, screen, play_button, sb, stats, ship, bullets, aliens):
    """更新屏幕函数"""
    # 重新绘制屏幕
    screen.fill(i_settings.bg_color)

    # 绘制飞船
    ship.generate()

    # 循环绘制子弹, sprites返回一个列表
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制外星人
    aliens.draw(screen)

    # 绘制分数
    sb.show_score()

    # 绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见（刷新屏幕）
    pygame.display.flip()


def delete_bullet(bullets):
    """子弹清空"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def fire_bullet(i_settings, screen, ship, bullets):
    """创建子弹数组"""
    if len(bullets) < i_settings.bullets_count:
        # 创建一颗子弹，并将其加入编组bullets中
        new_bullet = Bullet(i_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(i_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    alien = Alien(i_settings, screen)
    # 每行多少个
    number_aliens_x = get_number_aliens_x(i_settings, alien.rect.width)
    # 一共多少行
    number_aliens_y = get_number_aliens_y(i_settings, ship.rect.height, alien.rect.height)
    for y_number in range(number_aliens_y):
        for x_number in range(number_aliens_x):
            create_alien(i_settings, screen, aliens, y_number, x_number)


def get_number_aliens_x(i_settings, alien_width):
    """计算每行可容乃多少个外星人"""
    available_space_x = i_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_y(i_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (i_settings.screen_height - 3 * alien_height - ship_height)
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y


def create_alien(i_settings, screen, aliens, y_number, x_number):
    # 外星人的间距为一个外星人
    alien = Alien(i_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * x_number
    alien.y = alien_height + 2 * alien_height * y_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def update_aliens(i_settings, aliens):
    """检查是否有外星人到达屏幕边缘，并更新外星人的位置"""
    check_fleet_edges(i_settings, aliens)
    aliens.update()


def change_fleet_direction(i_settings, aliens):
    """将整群外星人下移"""
    for alien in aliens.sprites():
        alien.rect.y += i_settings.alien_fleet_drop_speed
    # 左移
    i_settings.alien_fleet_direction *= -1


def check_fleet_edges(i_settings, aliens):
    """有外星人到达屏幕边缘时采取相应的措施"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(i_settings, aliens)
            break


def check_high_score(stats, sb):
    """验证最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def aliens_bullets_to_hit(i_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹的位置, 并删除已消失的子弹"""
    # 检查是否有子弹集中了外星人,如果击中删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # 当有外星人与飞船发生碰撞，把分算上
        # 每次碰撞，字典的key都是一个列表，该列表包含所有与该子弹发生碰撞的外星人
        for aliens in collisions.values():
            stats.score += i_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # 提高难度
        i_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()

        # 删除现有的子弹并船舰一群外星人
        bullets.empty()
        create_fleet(i_settings, screen, ship, aliens)


def check_ship_hit(i_settings, screen, play_button, sb, stats, ship, aliens, bullets):
    # 如果飞船与外星人发生碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(i_settings, screen, play_button, sb, stats, ship, aliens, bullets)


def ship_hit(i_settings, screen, play_button, sb, stats, ship, aliens, bullets):
    """飞船与外星人碰撞处理函数"""
    # 碰撞结束
    if stats.ships_count > 0:
        stats.ships_count -= 1

        # 重置飞船数量显示
        sb.prep_ships()

        # 清空外星人泪飙和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(i_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)

        print(stats.ships_count)
        print("Ship hit!!!")
    else:
        stats.game_active = False
        # 使光标可见
        pygame.mouse.set_visible(True)


def check_aliens_bottom(i_settings, screen, play_button, sb, stats, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(i_settings, screen, play_button, sb, stats, ship, aliens, bullets)
            break


def check_play_button(i_settings, screen, sb, stats, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """在晚间单击Play按钮时开始新游戏"""
    # collidepoint 方法检查鼠标点击的位置是否再Play按钮的rect内
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 结束标记
        stats.game_active = True

        # 重置分数
        stats.reset_stats()
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 初始化游戏难度
        i_settings.initialize_dynamic_settings()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(i_settings, screen, ship, aliens)
        ship.center_ship()