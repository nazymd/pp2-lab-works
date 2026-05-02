import pygame
import random
import sys
from TSIS3.persistence import save_score, load_settings

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

LANES = [50, 140, 230, 320]


class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-50))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.centerx = random.choice(LANES)
        self.rect.y = -100

    def update(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.reset()


def play_game(username):
    settings = load_settings()

    player = Player(settings["car_color"])
    enemies = pygame.sprite.Group()

    for _ in range(3):
        enemies.add(Enemy())

    score = 0
    distance = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        player.update()
        enemies.update()

        distance += 0.1
        score = distance

        if pygame.sprite.spritecollideany(player, enemies):
            save_score(username, score, distance)
            return "menu"

        screen.fill((100,100,100))
        enemies.draw(screen)
        screen.blit(player.image, player.rect)

        pygame.display.flip()
        clock.tick(60)