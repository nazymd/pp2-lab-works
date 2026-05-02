import pygame
from collections import deque
import math


def draw_rect(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    rect = pygame.Rect(
        min(x1, x2),
        min(y1, y2),
        abs(x2 - x1),
        abs(y2 - y1)
    )

    pygame.draw.rect(surface, color, rect, size)


def draw_square(surface, color, start, end, size):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))

    x = start[0]
    y = start[1]

    if end[0] < start[0]:
        x -= side
    if end[1] < start[1]:
        y -= side

    pygame.draw.rect(surface, color, (x, y, side, side), size)


def draw_circle(surface, color, start, end, size):
    radius = int(math.dist(start, end))
    pygame.draw.circle(surface, color, start, radius, size)


def draw_right_triangle(surface, color, start, end, size):
    points = [
        start,
        (start[0], end[1]),
        end
    ]
    pygame.draw.polygon(surface, color, points, size)


def draw_equilateral_triangle(surface, color, start, end, size):
    x1, y1 = start 
    x2, y2 = end

    side = abs(x2 - x1)
    height = int(side * (3 ** 0.5) / 2)

    points = [
        (x1, y1),  
        (x1 - side // 2, y1 + height),
        (x1 + side // 2, y1 + height) 
    ]

    pygame.draw.polygon(surface, color, points, size)


def draw_rhombus(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(surface, color, points, size)


def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()

    if x < 0 or x >= width or y < 0 or y >= height:
        return

    old_color = surface.get_at((x, y))

    if old_color == new_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        px, py = queue.popleft()

        if px < 0 or px >= width or py < 0 or py >= height:
            continue

        if surface.get_at((px, py)) != old_color:
            continue

        surface.set_at((px, py), new_color)

        queue.append((px + 1, py))
        queue.append((px - 1, py))
        queue.append((px, py + 1))
        queue.append((px, py - 1))