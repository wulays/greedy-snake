import pygame
from pygame.sprite import Sprite

class Snake(Sprite):

    def __init__(self, game):

        super().__init__()

        self.body = [(200, 200)]
        self.screen = game.screen
        self.setting = game.setting
        self.direction = 'up'

    def move(self):
        (x, y) = self.body[0]

        match self.direction:
            case 'up':
                self.body.insert(0, (x, y - 10))
            case 'down':
                self.body.insert(0, (x, y + 10))
            case 'left':
                self.body.insert(0, (x - 10, y))
            case 'right':
                self.body.insert(0, (x + 10, y))
        self.body.pop()

    def change_direction(self, new_direction):
        if (new_direction == 'up' and self.direction != 'down' or
                new_direction == 'down' and self.direction != 'up' or
                new_direction == 'left' and self.direction != 'right' or
                new_direction == 'right' and self.direction != 'left'):
            self.direction = new_direction

    def add(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(self.screen, (0, 0, 0), (*segment, 10, 10))

    def check_hit_wall(self):
        (x, y) = self.body[0]
        if x >= self.screen.get_rect().right - self.setting.grid_width or x <= 0:
            return True
        elif y >= self.screen.get_rect().bottom - self.setting.grid_height or y <= 0:
            return True
        return False
