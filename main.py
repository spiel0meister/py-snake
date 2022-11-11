import pygame

WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
black = (0, 0, 0)

def draw():
    WIN.fill(black)
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
