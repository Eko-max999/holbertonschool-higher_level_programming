#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Tuple-lara (0, 0) elave edirik ki, index xetasi olmasin
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Ancaq ilk iki elementi cemleyirik
    return (a[0] + b[0], a[1] + b[1])
