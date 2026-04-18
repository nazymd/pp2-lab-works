# import pygame
# pygame.init()
# screen=pygame.display.set_mode((500, 500))
# running=True
# music1=pygame.mixer.Sound('songs/music1.mp3')
# music2=pygame.mixer.Sound('songs/music2.mp3')
# while running:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             running=False
#         if event.type==pygame.KEYDOWN:
#             if event.key == pygame.K_p:
#                 music1.play()
#             if event.key == pygame.K_s:
#                 pygame.mixer.music.stop()
#             if event.key == pygame.K_n:
#                 music2.play()
#             if event.key == pygame.K_b:
#                 music2.play()
#     font = pygame.font.SysFont("Verdana", 20)
#     screen.blit(font.render("P = pause/unpause, S = stop, R = restart", True, "white"), (10, 80))
#     pygame.display.flip()
            

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
running = True

music1 = pygame.mixer.Sound("songs/music1.mp3")
music2 = pygame.mixer.Sound("songs/music2.mp3")

current = 1

font = pygame.font.SysFont("Verdana", 20)

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                if current == 1:
                    music1.play()
                else:
                    music2.play()

            if event.key == pygame.K_s:
                music1.stop()
                music2.stop()

            if event.key == pygame.K_n:
                music1.stop()
                music2.stop()
                music2.play()
                current = 2

            if event.key == pygame.K_b:
                music1.stop()
                music2.stop()
                music1.play()
                current = 1

    text = font.render("P-Play S-Stop N-Next B-Back", True, "white")
    screen.blit(text, (20, 200))

    pygame.display.flip()

pygame.quit()