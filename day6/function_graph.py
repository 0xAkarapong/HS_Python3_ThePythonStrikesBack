import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    for x in range(w):
            y = f(x)
            if y < h:
                screen.set_at((x, h - y), (255, 255, 255))  # Invert y-axis for correct plotting


    pygame.display.flip()

pygame.quit()