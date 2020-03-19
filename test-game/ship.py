import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类"""

    def __init__(self, i_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.i_settings = i_settings

        # 加载飞船图像并获取外加矩形
        self.image = pygame.image.load('images/xfj.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 飞船属性
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def generate(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 如果右移按键按下为真与飞船图形的右边<窗口对象为真的话右移
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.i_settings.ship_speed_factor
        # 如果左移按键按下为真与飞船图形的左边>0的话左移
        if self.moving_left and self.rect.left > 0:
            self.center -= self.i_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        """飞船居中"""
        self.center = self.screen_rect.centerx
