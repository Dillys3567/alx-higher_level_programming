#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    my_list.reverse()
    for i in range(l):
        print("{:d}".format(my_list[i]))
