#!/usr/bin/python3
"""load json from a file"""
import json

def load_from_json_file(filename):
    """read a json object froma file"""
    with open(filename) as f:
        return json.load(f)
