import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, i_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.i_settings = i_settings

        # 加载外星人图像， 并设置其rect属性
        self.image = pygame.image.load('images/wxr.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def generate(self):
        """再指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动外星人"""
        self.x += (self.i_settings.alien_speed_factor * self.i_settings.alien_fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True