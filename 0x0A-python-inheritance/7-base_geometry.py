#!/usr/bin/python3

"""A class called
BaseGeometry"""
class BaseGeometry():
    """A function that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    """A function that validates value"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
