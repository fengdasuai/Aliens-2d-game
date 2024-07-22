class Settings :
    """储存游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (216,216,216)

        # 飞船速度设置
        self.ship_speed = 0.6

        # 子弹设置
        self.bullet_speed = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 100

        # 外星人设置
        self.alien_speed = 0.25
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        self.ship_limit = 3

        # 加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 0.6
        self.alien_speed = 0.5
        self.bullet_speed = 0.4

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)
