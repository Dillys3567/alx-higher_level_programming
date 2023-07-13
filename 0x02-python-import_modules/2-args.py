#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numArgs = len(argv)
    if numArgs == 1:
        print("{} arguments.".format(numArgs - 1))
    elif numArgs == 2:
        print("{} argument:".format(numArgs - 1))
        print("1: {}".format(argv[1]))
    elif numArgs > 2:
        print("{} arguments:".format(numArgs - 1))
        for i in range(1, numArgs):
            print("{}: {}".format(i, argv[i]))
