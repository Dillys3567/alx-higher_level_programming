#!/usr/bin/python3
"""write an object to text file in json"""
import json

def save_to_json_file(my_obj, filename):
    """write json object to text file 
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
