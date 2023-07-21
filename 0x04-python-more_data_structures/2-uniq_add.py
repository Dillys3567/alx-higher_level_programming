#!/usr/bin/python3

def uniq_add(my_list=[]):
    ulist = set(my_list)
    n = 0
    for i in ulist:
        n += i
    return n

