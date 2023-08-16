#!/usr/bin/python3

"""a class that defines student"""

class Student:
    """has public instance attributes"""
    def __init__(self, first_name, last_name, age):
        """instantiate attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrive dictionary representation of student"""
        return self.__dict__
