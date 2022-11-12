from itertools import product
from random import randint
from typing import Tuple
import pygame

WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

ROWS, COLS = 10, 10
CELL_WIDTH, CELL_HEIGHT = WIDTH / COLS, HEIGHT / ROWS

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def create_random_pos(x_range: Tuple[int, int], y_range: Tuple[int, int]):
        return Pos(randint(x_range[0], x_range[1]), randint(y_range[0], y_range[1]))


snake = [Pos.create_random_pos((0, COLS-1), (0, ROWS-1))]
food = Pos.create_random_pos((0, COLS-1), (0, ROWS-1))


def draw():
    WIN.fill(black)

    for pos in snake:
        pygame.draw.rect(WIN, red, (pos.x * CELL_WIDTH,
                         pos.y * CELL_HEIGHT, CELL_WIDTH - 1, CELL_HEIGHT - 1))

    pygame.draw.rect(WIN, yellow, (food.x * CELL_WIDTH,
                                   food.y * CELL_HEIGHT, CELL_WIDTH - 1, CELL_HEIGHT - 1))

    pygame.display.update()


def while_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()


def main(): while_loop()


if __name__ == "__main__":
    main()
