from random import randint
from typing import Tuple


class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def create_random_pos(x_range: Tuple[int, int], y_range: Tuple[int, int]):
        return Pos(randint(x_range[0], x_range[1]), randint(y_range[0], y_range[1]))

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def __mul__(self, num):
        return Pos(self.x * num, self.y * num)

    def __str__(self): return f"({self.x}, {self.y})"


class Snake:
    def __init__(self, head_x: int, head_y: int):
        self.body = [Pos(head_x, head_y)]
        self.state = None

    def draw(self, pygame, WIN, color, W, H):
        for pos in self.body:
            pygame.draw.rect(WIN, color, (pos.x * W,
                                          pos.y * H, W - 1, H - 1))

    def update(self, rows, cols):
        i = len(self.body) - 1
        while i > 0:
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
            i -= 1
        state = self.state
        if state == 0:
            self.head.y = (self.head.y - 1 + rows) % rows
        elif state == 1:
            self.head.x = (self.head.x + 1 + cols) % cols
        elif state == 2:
            self.head.y = (self.head.y + 1 + rows) % rows
        elif state == 3:
            self.head.x = (self.head.x - 1 + cols) % cols
        return any(pos.x == self.head.x and pos.y == self.head.y for pos in self.body[1:])

    def pick_up_food(self, food):
        if food.x != self.head.x or food.y != self.head.y:
            return False
        if len(self.body) == 1:
            state = self.state
            if state == 0:
                self.body.append(Pos(self.head.x, self.head.y+1))
            elif state == 1:
                self.body.append(Pos(self.head.x - 1, self.head.y))
            elif state == 2:
                self.body.append(Pos(self.head.x, self.head.y-1))
            elif state == 3:
                self.body.append(Pos(self.head.x + 1, self.head.y))
        else:
            p1 = self.body[len(self.body) - 1]
            p2 = self.body[len(self.body) - 2]
            p_new = p1 * 2 - p2
            self.body.append(p_new)
        return True

    @property
    def head(self) -> Pos: return self.body[0]
