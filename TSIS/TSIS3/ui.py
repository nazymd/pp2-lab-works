import pygame
import sys
from TSIS3.persistence import load_leaderboard, load_settings, save_settings

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font_big = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)
clock = pygame.time.Clock()


def draw_text(text, font, color, x, y, center=False):
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(img, rect)


def button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (180, 180, 180), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    draw_text(text, font_small, (0, 0, 0), x + w//2, y + h//2, True)

    if rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pygame.time.delay(150)
            return True
    return False


def username_screen():
    name = ""

    while True:
        screen.fill((255,255,255))
        draw_text("Enter name", font_big, (0,0,0), WIDTH//2, 150, True)
        draw_text(name, font_small, (0,0,0), WIDTH//2, 250, True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        pygame.display.flip()
        clock.tick(60)


def leaderboard_screen():
    data = load_leaderboard()

    while True:
        screen.fill((255,255,255))
        draw_text("Leaderboard", font_big, (0,0,0), WIDTH//2, 50, True)

        y = 120
        for i, item in enumerate(data):
            txt = f"{i+1}. {item['name']} {item['score']}"
            draw_text(txt, font_small, (0,0,0), 50, y)
            y += 30

        if button("Back", 120, 500, 160, 40):
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        pygame.display.flip()
        clock.tick(60)


def settings_screen():
    settings = load_settings()

    while True:
        screen.fill((255,255,255))

        draw_text("Settings", font_big, (0,0,0), WIDTH//2, 50, True)

        if button("Toggle Sound", 100, 200, 200, 40):
            settings["sound"] = not settings["sound"]

        if button("Save & Back", 100, 300, 200, 40):
            save_settings(settings)
            return

        pygame.display.flip()
        clock.tick(60)


def main_menu():
    while True:
        screen.fill((255,255,255))

        draw_text("RACER", font_big, (0,0,0), WIDTH//2, 100, True)

        if button("Play", 120, 200, 160, 40):
            return "play"

        if button("Leaderboard", 120, 260, 160, 40):
            leaderboard_screen()

        if button("Settings", 120, 320, 160, 40):
            settings_screen()

        if button("Quit", 120, 380, 160, 40):
            pygame.quit(); sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        pygame.display.flip()
        clock.tick(60)