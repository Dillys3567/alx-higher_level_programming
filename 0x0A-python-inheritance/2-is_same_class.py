#!/usr/bin/python3

"""A function tha returns true if the object
is an instance of a specified class else false
"""
def is_same_class(obj, a_class):
    """check if object is an
    instance of specified class
    """
    return (True if (type(obj) == a_class) else  False)
