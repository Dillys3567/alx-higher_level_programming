#!/usr/bin/python3

"""class square"""
class Square:
    """init"""
    def __init__(self, size=0):
        """attributes"""
        self.__size = size
    """get size"""
    def size(self):
        return (self.__size)
    """set size"""
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """area"""
    def area(self):
        return (self.__size ** 2)

