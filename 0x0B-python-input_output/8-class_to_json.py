#!/usr/bin/python3
"""return dictionary description of object"""

def class_to_json(obj):
    """return dictionary descriptionof class instance
    obj"""
    return obj.__dict__
