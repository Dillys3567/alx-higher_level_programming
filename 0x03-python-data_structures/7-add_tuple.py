#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    fir1 = fir2 = las1 = las2 = 0
    if len(tuple_a) < 2:
        if len(tuple_a) < 1:
            fir1 = 0
            las1 = 0
        else:
            fir1 = tuple_a[0]
            las1 = 0
    else:
        fir1 = tuple_a[0]
        las1 = tuple_a[1]
    if len(tuple_b) < 2:
        if len(tuple_b) < 1:
            fir2 = 0
            las2 = 0;
        else:
            las2 = 0
            fir2 = tuple_b[0]
    else:
        las2 = tuple_b[1]
        fir2 = tuple_b[0]
    a = fir1 + fir2
    b = las1 + las2
    return (a,b)
