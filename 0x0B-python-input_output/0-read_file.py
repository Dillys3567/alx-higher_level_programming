#!/usr/bin/python3
"""A text file reading function."""

def read_file(filename=""):
    """Print the file contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
