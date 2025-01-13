import pygame

class Circle:
    def __init__(self, radius: float, x: int, y: int, screen_width: int, screen_height: int):
        self.radius = radius
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.dx = 5 # Speed
        self.dy = 5 # Speed

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

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
    circle = Circle(20, 100, 100, width, height)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        circle.move()
        circle.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()