from random import choice


class RandomWalk:
    """一个僧成随机漫步数据得类"""

    def __init__(self, num_points=50000):
        """初始化随机漫步得属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            # 决定前进方向 (left, right)
            x_direction = choice([1, -1])
            # 移动的距离
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            # 决定移动的方向（up ,down)
            y_direction = choice([1, -1])
            # 移动的距离
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点得x和y值([-1]得到数组最后一个值)
            nest_x = self.x_values[-1] + x_step
            nest_y = self.y_values[-1] + y_step

            self.x_values.append(nest_x)
            self.y_values.append(nest_y)