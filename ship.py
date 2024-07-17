import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其起始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置。"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -=self.settings.ship_speed

        if self.moving_down and self.rect.bottom <self.screen_rect.bottom :
            self.y +=self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)