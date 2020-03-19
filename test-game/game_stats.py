class GameStats:
    def __init__(self, i_settings):
        """初始化统计信息"""
        # 开始结束标记
        self.game_active = False

        # 最高分数记录
        self.high_score = 0
        self.old_high_score = 0

        # 飞船等级
        self.level = 1

        self.i_settings = i_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_count = self.i_settings.ship_limit
        self.score = 0