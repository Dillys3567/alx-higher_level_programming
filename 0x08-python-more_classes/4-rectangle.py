#!/usr/bin/python3

"""Rectangle class"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """initialise class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    def area(self):
        """area of rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """perimeter of rect"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """str or print"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string

        for i in range(self.height):
            for j in range(self.width):
                string += '#'
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """repr method"""
        string = "Rectangle("
        string += str(self.width)
        string += ", " + str(self.height) + ")"
        return string
