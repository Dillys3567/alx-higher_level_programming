#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if 97 <= ord(w) <= 122:
            upper = chr(ord(w) - 32)
        else:
            upper = w
        print("{}".format(upper), end='')
    print()
