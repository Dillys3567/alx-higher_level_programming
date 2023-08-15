#!/usr/bin/python3

""" A function that tells if 
an object is an instance of a class"""
def is_kind_of_class(obj, a_class):
    """This inheritance is for both
    direct and indirect"""
    return (True if (isinstance(obj, a_class)) else False)
