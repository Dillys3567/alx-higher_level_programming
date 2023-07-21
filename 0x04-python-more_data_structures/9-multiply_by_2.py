#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    l = list(new.keys())

    for i in l:
        new[i] *= 2
    return new
