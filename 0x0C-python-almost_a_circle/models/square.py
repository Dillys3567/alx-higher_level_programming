#!/usr/bin/python3
"""A square class inheriting from rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """constructor method for square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print object"""
        string = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)
        return string

    @property
    def size(self):
        """getter for size"""
        return self.height

    @size.setter
    def size(self, val):
        """setter for size"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """update using arguments"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init(self,size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
