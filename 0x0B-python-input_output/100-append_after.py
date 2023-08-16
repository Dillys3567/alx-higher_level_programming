#!/usr/bin/python3
"""a function that prints a string after a line in a file
"""

def append_after(filename="", search_string="", new_string=""):
    """insert text after each line containing a given string"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
