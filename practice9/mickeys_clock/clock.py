import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((1536, 1024))
WHITE = (255, 255, 255)
CLOCK_CENTER = (760, 360)

image_sur = pygame.image.load('images/clock.png')
mickey = pygame.image.load('images/main.png')
hand_left = pygame.image.load('images/hand_left_centered.png')
hand_right = pygame.image.load('images/hand_right_centered.png')
image_surface=pygame.transform.scale(image_sur, (1536, 1024))
mouse = pygame.transform.scale(mickey, (400, 400))
hand_l=pygame.transform.scale(hand_left, (300, 700))
hand_r=pygame.transform.scale(hand_right, (300, 700))

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(image_surface, (0, 0))

    now = datetime.datetime.now()

    m = now.minute
    s = now.second

    minutes_angle = -(m * 6 + s * 0.1)
    seconds_angle = -(s * 6)

    rotated_minutes = pygame.transform.rotate(hand_r, minutes_angle)
    rotated_seconds = pygame.transform.rotate(hand_l, seconds_angle)

    minutes_rect = rotated_minutes.get_rect(center=(770, 500))
    seconds_rect = rotated_seconds.get_rect(center=(770, 500))

    mic_rect = mouse.get_rect(center=(770, 500))

    screen.blit(rotated_minutes, minutes_rect)
    screen.blit(rotated_seconds, seconds_rect)
    screen.blit(mouse, mic_rect)

    pygame.display.flip()
pygame.quit()
