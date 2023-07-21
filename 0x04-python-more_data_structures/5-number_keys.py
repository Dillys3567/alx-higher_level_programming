#!/usr/bin/python3

def number_keys(a_dictionary):
    n = 0
    l = list(a_dictionary.keys())
    for i in l:
        n += 1
    return n
