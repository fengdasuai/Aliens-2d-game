import pygame
from pygame.sprite import Sprite
import settings

class Alien(Sprite):
    """单个外星人的类"""

    def __init__(self,ai_game):
        """初始化外星人的位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """向右移动外星人"""
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True