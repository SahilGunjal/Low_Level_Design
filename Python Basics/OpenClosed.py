from abc import abstractmethod, ABC

"""
open-Closed principle: It states that the software modules(classes, modules, functions) should open for extension
but closed for modification
"""


class ShapePropertiesCalculator:
    def calculateArea(self, shape):
        if shape.type == "circle":
            return 3.14 * shape.radius ** 2
        elif shape.type == "rectangle":
            return shape.len * shape.width

    def calculatePerimeter(self, shape):
        if shape.type == "circle":
            return 2 * 3.14 * shape.radius
        elif shape.type == "rectangle":
            return 2 * (shape.len + shape.width)

    # if need to add one more shape let's say triangle then we need to make changes in this code
    # This is not following OCP and changing the class or adding methods in same can induce bugs


# Solution for this is to create a separate shape abstract class and extend the

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

    def calculatePerimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculateArea(self):
        return 3.14 * self.__radius ** 2

    def calculatePerimeter(self):
        return 2 * 3.14 * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__len = height
        self.__width = width

    def calculateArea(self):
        return self.__len * self.__width

    def calculatePerimeter(self):
        return 2 * (self.__len + self.__width)

# Later very easily we can add another class here for another shape
