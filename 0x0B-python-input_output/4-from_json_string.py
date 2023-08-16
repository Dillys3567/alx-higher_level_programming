#!/usr/bin/python3
"""return a json string object"""
import json

def from_json_string(my_str):
    """return python object representation of a
    json string"""
    return json.loads(my_str)
