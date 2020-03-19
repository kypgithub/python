import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """显示得分信息"""

    def __init__(self, i_settings, screen, stats):
        """初始化显示的粉涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.i_settings = i_settings
        self.stats = stats

        self.prep_ships()

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 读取本地最高分
        self.high_score_file = 'E:/download/python/high_score_file.txt'
        self.red_file_high_score()

        # 最高分
        self.prep_high_score()
        # 准备初始得分图像
        self.prep_score()

        # 飞船等级
        self.prep_level()

        # 创建飞船数组
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        # round函数表示精确到小数位多少位，负数表示取10倍数
        round_score = round(self.stats.score, -1)

        # 格式化分数显示，插入逗号分隔符
        score_str = "{:,}".format(round_score)

        # 创建分数对象
        self.score_image = self.font.render(score_str, True, self.text_color, self.i_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """创建最高分图像函数"""
        # round函数表示精确到小数位多少位，负数表示取10倍数
        high_score = round(self.stats.high_score, -1)

        # 格式化分数显示，插入逗号分隔符
        score_str = "{:,}".format(high_score)

        # 创建分数对象
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.i_settings.bg_color)

        # 将最高分居中
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.i_settings.bg_color)
        # 将等级放在得分的下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """将分数渲显示到屏幕"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 对数组调用 draw方法将绘制数组中的每个元素
        self.ships.draw(self.screen)

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_count):
            ship = Ship(self.i_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def red_file_high_score(self):
        str = ''
        try:
            with open(self.high_score_file) as file_object:
                str = file_object.read()
        except FileNotFoundError:
            print("No such file or directory " + self.high_score_file + "\n")
        else:
            if str != '':
                self.stats.old_high_score = int(str)
                self.stats.high_score = self.stats.old_high_score
                self.prep_high_score()

    def write_file_high_score(self):
        with open(self.high_score_file, 'w') as file_object:
            file_object.write(str(self.stats.high_score))
