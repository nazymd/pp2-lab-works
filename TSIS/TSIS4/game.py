import pygame
import random
import json
from db import save_result, get_best

pygame.init()

TILE = 20
COLS = 30
ROWS = 30
TOP = 40

WIDTH = COLS * TILE
HEIGHT = ROWS * TILE + TOP

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)


# ---------- SETTINGS ----------
def load_settings():
    with open("settings.json") as f:
        return json.load(f)


settings = load_settings()


# ---------- SNAKE ----------
class Snake:
    def __init__(self):
        self.body = [[15, 15]]
        self.dx = 1
        self.dy = 0
        self.grow = False

    def move(self):
        head = [self.body[0][0] + self.dx, self.body[0][1] + self.dy]
        self.body.insert(0, head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self):
        for part in self.body:
            c, r = part
            pygame.draw.rect(screen, settings["snake_color"],
                             (c*TILE, TOP+r*TILE, TILE, TILE))

    def hit_wall(self):
        c, r = self.body[0]
        return c < 0 or c >= COLS or r < 0 or r >= ROWS

    def hit_self(self):
        return self.body[0] in self.body[1:]

    def shorten(self):
        if len(self.body) > 2:
            self.body.pop()
            self.body.pop()


# ---------- FOOD ----------
class Food:
    def __init__(self):
        self.pos = [10, 10]

    def spawn(self, blocked):
        while True:
            self.pos = [random.randint(0, COLS-1), random.randint(0, ROWS-1)]
            if self.pos not in blocked:
                break

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.pos[0]*TILE, TOP+self.pos[1]*TILE, TILE, TILE))


class Poison:
    def __init__(self):
        self.pos = [5, 5]

    def spawn(self, blocked):
        while True:
            self.pos = [random.randint(0, COLS-1), random.randint(0, ROWS-1)]
            if self.pos not in blocked:
                break

    def draw(self):
        pygame.draw.rect(screen, (120, 0, 0),
                         (self.pos[0]*TILE, TOP+self.pos[1]*TILE, TILE, TILE))


# ---------- GAME ----------
def run_game(username):

    snake = Snake()
    food = Food()
    poison = Poison()

    score = 0
    level = 1
    speed = 8

    best = get_best(username)

    food.spawn(snake.body)
    poison.spawn(snake.body)

    running = True

    while running:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    snake.dx, snake.dy = 1, 0
                if e.key == pygame.K_LEFT:
                    snake.dx, snake.dy = -1, 0
                if e.key == pygame.K_UP:
                    snake.dx, snake.dy = 0, -1
                if e.key == pygame.K_DOWN:
                    snake.dx, snake.dy = 0, 1

        snake.move()

        if snake.hit_wall() or snake.hit_self():
            save_result(username, score, level)
            return

        if snake.body[0] == food.pos:
            snake.grow = True
            score += 1

            if score % 5 == 0:
                level += 1
                speed += 1

            food.spawn(snake.body)

        if snake.body[0] == poison.pos:
            snake.shorten()

            if len(snake.body) <= 1:
                save_result(username, score, level)
                return

            poison.spawn(snake.body)

        screen.fill((30, 30, 30))

        snake.draw()
        food.draw()
        poison.draw()

        text = font.render(
            f"{username} Score:{score} Level:{level} Best:{best}",
            True, (255, 255, 255)
        )
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(speed)