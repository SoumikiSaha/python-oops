from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Create objects
rectangle = Rectangle(10, 5)
circle = Circle(7)
square = Square(4)

# Display Rectangle details
print("Rectangle")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

# Display Circle details
print("\nCircle")
print("Area:", round(circle.area(), 2))
print("Perimeter:", round(circle.perimeter(), 2))

# Display Rectangle details
print("\nSquare")
print("Area:", square.area())
print("Perimeter:", square.perimeter())
