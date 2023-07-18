import sys
import time

import pygame
from setting import Setting
from food import Food
from snake import Snake

class Game:

    def __init__(self):

        pygame.init()
        self.setting = Setting()
        pygame.display.set_caption('Snake Demo')
        self.screen = pygame.display.set_mode((self.setting.width, self.setting.height))

        self.foods = pygame.sprite.Group()


    def run_game(self):
        clock = pygame.time.Clock()
        self.snake = Snake(self)

        while True:


            self._check_events()

            self._create_food()

            self._update_screen()
            clock.tick(24)

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('down')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('left')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('right')

    def _create_food(self):

        if len(self.foods) < 1:
            food = Food(self)
            self.foods.add(food)

    def _update_screen(self):
        self.screen.fill(self.setting.bgColor)
        self.snake.move()
        self.foods.draw(self.screen)
        self.snake.draw()
        for food in self.foods.sprites():
            if self.snake.body[0] == (food.rect.x, food.rect.y):
                self.foods.remove(food)
                self.snake.add()
        pygame.display.flip()



if __name__ == '__main__':

    game = Game()
    game.run_game()