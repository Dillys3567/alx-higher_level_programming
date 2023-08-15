#!/usr/bin/python3

"""A class called my_list
which inherits from list"""
class MyList(list):
    """a function that prints sorted
    in ascending order"""
    def print_sorted(self):
        print(sorted(self))
