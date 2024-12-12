from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod   # python version > 3.4


# class Shape(metaclass=ABCMeta):
class Shape(ABC):  # python version > 3.4

    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape, ABC):
    type = 'Rectangle'
    sides = 4

    def __init__(self):
        self.length = 4
        self.breadth = 5

    def print_area(self):
        return self.length * self.breadth


rect = Rectangle()
print(rect.print_area())  # output: 20

