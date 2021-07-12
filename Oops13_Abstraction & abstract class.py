# Abstraction is used to hide the internal functionality of the function from the users.
# The users only interact with the basic implementation of the function, but inner working is hidden.
# In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
# It also enhances the application efficiency.
# In Python, abstraction can be achieved by using abstract classes

# Abstract Base Class
# Abstract methods do not contain their implementation
# Abstraction classes are meant to be the blueprint of the other class.
# we can not make objects of abstract base class
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def area(self):
        return self.length * self.breadth
    pass

    def parameter(self):
        return 2 * (self.length + self.breadth)


class Square(Shape):
    side = 4

    def area(self):
        return self.side * self.side
    pass

    def parameter(self):
        return 4 * self.side
    pass


class Child_Square(Square):
    pass


rect = Rectangle()
sq = Square()
child = Child_Square()
