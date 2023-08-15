#!/usr/bin/python3

"""A function that adds new attributes to an 
object if possible"""

def add_attribute(obj, att, value):
    """Add anew attribute to object if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
