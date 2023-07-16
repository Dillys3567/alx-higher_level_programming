#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    nargs = len(argv)
    if nargs != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    elif nargs == 4:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif op == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("{}".format("Unknown operator. Available operators: +, -, * and /"))
            exit(1)
