#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    l = list(a_dictionary.keys())

    for v in l:
        if value == a_dictionary.get(v):
            del a_dictionary[v]

    return a_dictionary
