class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is Circle with an area of {3.14 * (self.radius ** 2)}")


class Square(Shape):

    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle(color="red", is_filled=True, radius=5)
print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()
circle.describe()
