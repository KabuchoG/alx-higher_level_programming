#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    for i, j in res.items():
        res[i] = j * 2
    return res
