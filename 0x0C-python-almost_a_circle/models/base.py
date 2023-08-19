#!/usr/bin/python3
"""A class called Base"""

class Base:
    """Base class with private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the class"""
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
