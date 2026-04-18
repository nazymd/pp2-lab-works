import pygame
pygame.init()
screen=pygame.display.set_mode((800,800))
WHITE=(255, 255, 255)
RED=(255, 0, 0)
x,y=400,400
r=25
step=20
running=True
while running:
    screen.fill('White')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-=step
            if event.key == pygame.K_RIGHT:
                x+=step
            if event.key == pygame.K_UP:
                y -= step
            if event.key == pygame.K_DOWN:
                y += step
    if x < r:
        x = r

    if x > 775:
        x = 775

    if y < r:
        y = r

    if y > 775:
        y = 775

    pygame.draw.circle(screen, RED, (x, y), r)

    pygame.display.flip()