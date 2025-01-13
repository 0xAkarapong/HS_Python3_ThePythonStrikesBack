class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self) -> None:
        print(f"{self.x}, {self.y}")

    def move(self) -> None:
        self.x += 1
        self.y += 1

if __name__ == "__main__":
    c = Circle(10, 100, 100)
    c.draw()
    c.move()
    c.draw()
