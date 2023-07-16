#!/usr/bin/python3

def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        fc = None
    else:
        fc = sentence[0]

    return (l, fc)

