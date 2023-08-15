#!/usr/bin/python3

"""Rectangle class from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):

    """instantiate with width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """a function that returns the area"""
    def area(self):
        """An area function"""
        return (self.__width * self.__height)

    def __str__(self):
        """return the print() and str() representation of a
        Rectangle"""
        string = "[{}] ".format(str(self.__class__.__name__))
        string += str(self.__width) + "/" + str(self.__height)
        return string
