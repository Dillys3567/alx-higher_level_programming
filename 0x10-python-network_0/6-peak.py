#!/usr/bin/python3
"""script for finding peak in list of ints
"""

def find_peak(list_of_integers):
    """forced implementation
    """
    maxs = None
    for i in list_of_integers:
        if maxs is None or maxs < i:
            maxs = i
    return maxs
