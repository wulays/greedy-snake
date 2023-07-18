import pygame
from pygame.sprite import Sprite
import random

class Food(Sprite):

    def __init__(self, game):

        super().__init__()

        self.setting = game.setting
        self.screen = game.screen

        self.image = pygame.Surface((self.setting.food_width, self.setting.food_height))
        self.rect = pygame.Rect(0, 0, self.setting.food_width, self.setting.food_height)
        self.rect.x = random.randint(0, self.setting.width / 10) * 10 - 10
        self.rect.y = random.randint(0, self.setting.height / 10) * 10 - 10