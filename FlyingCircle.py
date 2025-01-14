import pygame
import random
import sys

class Circle:
    def __init__(self, radius: float, x: int, y: int, screen_width: int, screen_height: int):
        self.radius = radius
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.dx = self.dy = 2
        self.red = random.randint(0,255)
        self.green = random.randint(0,255)
        self.blue = random.randint(0,255)
        self.dc_red = 1
        self.dc_green = 1
        self.dc_blue = 1
        self.color = (self.red, self.green, self.blue)

    def draw(self, screen: pygame.Surface) -> None:
        self.color = (self.red, self.green, self.blue)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.red >= 255 or self.red <= 0:
            self.dc_red *= -1
        if self.green >= 255 or self.green <= 0:
            self.dc_green *= -1
        if self.blue >= 255 or self.blue <= 0:
            self.dc_blue *= -1
        self.red += self.dc_red
        self.green += self.dc_green
        self.blue += self.dc_blue

    def move(self) -> None:
        self.x += self.dx
        self.y += self.dy

        if self.x + self.radius > self.screen_width or self.x - self.radius < 0:
            self.dx *= -1
        if self.y + self.radius > self.screen_height or self.y - self.radius < 0:
            self.dy *= -1

def main():
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Flying Circle")
    circle_list = []
    for _ in range(25):
        circle_list.append(Circle(random.randint(10, 25), random.randint(0, width), random.randint(0, height), width, height))
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for circle in circle_list:
            circle.move()
            circle.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()