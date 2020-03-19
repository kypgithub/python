class Settings:
    """配置类"""

    def __init__(self):
        """初始化游戏的配置"""
        # 窗口
        self.screen_width = 800
        self.screen_height = 460
        # 背景色
        self.bg_color = (0, 0, 0)

        # 飞船数量
        self.ship_limit = 3

        # 子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_count = 100

        # 外星人
        # 下移距离
        self.alien_fleet_drop_speed = 10
        # fleet_direction为1表示右移，-1表示左移
        self.alien_fleet_direction = 1

        # 游戏难度
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

        # 开始按钮
        self.play_button_msg = "Play"

    def initialize_dynamic_settings(self):
        """初始化游戏数据"""
        self.ship_speed_factor = 0.3
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.3
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏难度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale