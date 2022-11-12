from itertools import product
import pygame
from random import randint

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


snake = [Pos(randint(0, COLS-1), randint(0, ROWS-1))]


def draw():
    WIN.fill(black)

    for pos in snake:
        pygame.draw.rect(WIN, red, (pos.x * CELL_WIDTH,
                         pos.y * CELL_HEIGHT, CELL_WIDTH - 1, CELL_HEIGHT - 1))

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
