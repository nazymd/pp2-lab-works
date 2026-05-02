import pygame
from datetime import datetime
from tools import *

pygame.init()

WIDTH, HEIGHT = 1100, 700
TOOLBAR_HEIGHT = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill("white")

font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

color = (0, 0, 0)
brush_size = 5
tool = "pencil"

drawing = False
start_pos = None
last_pos = None

text_mode = False
text_pos = None
text_value = ""

tools = [
    "pencil", "line", "rect", "circle",
    "square", "right_tri", "eq_tri",
    "rhombus", "fill", "text", "eraser", "clear"
]

colors = [
    (0, 0, 0), (255, 255, 255),
    (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (255, 255, 0),
    (255, 165, 0), (128, 0, 128)
]


def get_canvas_pos(pos):
    return pos[0], pos[1] - TOOLBAR_HEIGHT


def save_canvas():
    filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
    pygame.image.save(canvas, filename)
    print("Saved:", filename)


def draw_toolbar():
    pygame.draw.rect(screen, (220, 220, 220), (0, 0, WIDTH, TOOLBAR_HEIGHT))

    x = 10
    for t in tools:
        rect = pygame.Rect(x, 10, 85, 30)
        pygame.draw.rect(screen, (180, 180, 180), rect)

        if tool == t:
            pygame.draw.rect(screen, (0, 0, 0), rect, 3)

        text = font.render(t, True, (0, 0, 0))
        screen.blit(text, (x + 5, 17))

        x += 95

    x = 10
    for c in colors:
        rect = pygame.Rect(x, 55, 30, 30)
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 3)
        x += 40

    info = font.render(f"Size: {brush_size}   Press 1/2/3   Ctrl+S Save", True, (0, 0, 0))
    screen.blit(info, (380, 62))


def draw_shape(surface, selected_tool, start, end):
    if selected_tool == "line":
        pygame.draw.line(surface, color, start, end, brush_size)

    elif selected_tool == "rect":
        draw_rect(surface, color, start, end, brush_size)

    elif selected_tool == "circle":
        draw_circle(surface, color, start, end, brush_size)

    elif selected_tool == "square":
        draw_square(surface, color, start, end, brush_size)

    elif selected_tool == "right_tri":
        draw_right_triangle(surface, color, start, end, brush_size)

    elif selected_tool == "eq_tri":
        draw_equilateral_triangle(surface, color, start, end, brush_size)

    elif selected_tool == "rhombus":
        draw_rhombus(surface, color, start, end, brush_size)


running = True

while running:
    screen.fill("white")
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------- TEXT ----------
        if text_mode:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_value, True, color)
                    canvas.blit(text_surface, text_pos)
                    text_mode = False
                    text_value = ""

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_value = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_value = text_value[:-1]
                else:
                    text_value += event.unicode

        else:
            # ---------- KEYBOARD ----------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    brush_size = 2
                elif event.key == pygame.K_2:
                    brush_size = 5
                elif event.key == pygame.K_3:
                    brush_size = 10
                elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    save_canvas()

            # ---------- MOUSE DOWN ----------
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # toolbar
                if y < TOOLBAR_HEIGHT:
                    if 10 <= y <= 40:
                        index = (x - 10) // 95
                        if 0 <= index < len(tools):
                            tool = tools[index]

                    elif 55 <= y <= 85:
                        index = (x - 10) // 40
                        if 0 <= index < len(colors):
                            color = colors[index]

                else:
                    pos = get_canvas_pos(event.pos)

                    if tool == "fill":
                        flood_fill(canvas, pos[0], pos[1], color)

                    elif tool == "clear":
                        canvas.fill("white")

                    elif tool == "text":
                        text_mode = True
                        text_pos = pos
                        text_value = ""

                    else:
                        drawing = True
                        start_pos = pos
                        last_pos = pos

            # ---------- DRAW ----------
            if event.type == pygame.MOUSEMOTION and drawing:
                pos = get_canvas_pos(event.pos)

                if tool == "pencil":
                    pygame.draw.line(canvas, color, last_pos, pos, brush_size)
                    last_pos = pos

                elif tool == "eraser":
                    pygame.draw.line(canvas, (255, 255, 255), last_pos, pos, brush_size)
                    last_pos = pos

            # ---------- MOUSE UP ----------
            if event.type == pygame.MOUSEBUTTONUP and drawing:
                end_pos = get_canvas_pos(event.pos)

                if tool not in ["pencil", "eraser"]:
                    draw_shape(canvas, tool, start_pos, end_pos)

                drawing = False

    # ---------- PREVIEW ----------
    if drawing and tool not in ["pencil", "eraser"]:
        preview = canvas.copy()
        end_pos = get_canvas_pos(mouse_pos)
        draw_shape(preview, tool, start_pos, end_pos)
        screen.blit(preview, (0, TOOLBAR_HEIGHT))

    # ---------- TEXT PREVIEW ----------
    if text_mode:
        text_surface = font.render(text_value, True, color)
        screen.blit(text_surface, (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT))

    draw_toolbar()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()