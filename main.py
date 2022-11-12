from random import randint
import pygame
import Snake

WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

ROWS, COLS = 10, 10
CELL_WIDTH, CELL_HEIGHT = WIDTH / COLS, HEIGHT / ROWS

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)


def create_food(snake_body):
    random_pos = None
    free = False
    while not free:
        random_pos = Snake.Pos.create_random_pos((0, COLS-1), (0, ROWS-1))
        free = True
        for pos in snake_body:
            if pos.x == random_pos.x and pos.y == random_pos.y:
                random_pos = Snake.Pos.create_random_pos(
                    (0, COLS-1), (0, ROWS-1))
                free = False
    return random_pos


# STATES:
#    0: UP
#    1: RIGHT
#    2: DOWN
#    3: LEFT


def draw(snake, food):
    WIN.fill(black)

    pygame.draw.rect(WIN, yellow, (food.x * CELL_WIDTH,
                                   food.y * CELL_HEIGHT, CELL_WIDTH - 1, CELL_HEIGHT - 1))

    snake.draw(pygame, WIN, red, CELL_WIDTH, CELL_HEIGHT)

    pygame.display.update()


def while_loop():
    snake = Snake.Snake(randint(0, COLS-1), randint(0, ROWS-1))
    food = create_food(snake.body)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.state = 0
                elif event.key == pygame.K_d:
                    snake.state = 1
                elif event.key == pygame.K_s:
                    snake.state = 2
                elif event.key == pygame.K_a:
                    snake.state = 3

        if snake.pick_up_food(food):
            food = create_food(snake.body)
        snake.update()
        draw(snake, food)
        CLOCK.tick(5)


def main(): while_loop()


if __name__ == "__main__":
    main()
