import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x ** 2

pygame.init()

w = 600
h = 600

x_min, x_max = -2, 2
y_min, y_max = 0, 4

x_scale = w / (x_max - x_min)
y_scale = h / (y_max - y_min)

x_origin = w // 2
y_origin = h // 2

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    for pixel_x in range(w):
            x = x_min + pixel_x / x_scale
            y = f(x)
            pixel_y = h - int((y - y_min) * y_scale)
            if y < h:
                screen.set_at((pixel_x, pixel_y), (255, 255, 255)) 


    pygame.display.flip()

pygame.quit()