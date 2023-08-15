#!/usr/bin/python3

"""A Square class inheriting from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class square inheriting from Rectangle"""

    def  __init__(self, size):
        """instantiating a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
