#!/usr/bin/python3

"""Show if object inherits
directly or indirectly from a class"""
def inherits_from(obj, a_class):
    """The object inherits directly or
    indirectly"""
    return (True if (isinstance(obj, a_class) and  type(obj) != a_class) else False)
