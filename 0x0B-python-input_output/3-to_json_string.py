#!/usr/bin/python3
""" string to json function"""
import json

def to_json_string(my_obj):
    """return json representation
    of a string object
    """
    return json.dumps(my_obj)
