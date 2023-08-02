#!/usr/bin/python3

"""class square"""
class Square:
    """init"""
    def __init__(self, size=0):
        """instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= o")

        self.__size = size

    """instance method"""
    def area(self):
        return (self.__size ** 2)

