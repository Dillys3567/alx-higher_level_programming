#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    lastdig = number % 10
    print("{:d}".format(lastdig), end='')
    return lastdig
