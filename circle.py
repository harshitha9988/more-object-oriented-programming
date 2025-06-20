import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

a = Circle(5)
print(f"Area: {a.area():.2f}")
print(f"Perimeter: {a.perimeter():.2f}")