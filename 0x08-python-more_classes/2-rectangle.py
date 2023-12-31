#!/usr/bin/python3

"""Rectangle class"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """initialisation function"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method for area"""
        return (self.height * self.width)

    def perimeter(self):
        """method for perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))
