#!/usr/bin/python3
"""a file appending function"""

def append_write(filename="", text=""):
    """appends a string to the
    end of a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
