#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = {}
    for i in a_dictionary:
        res += i 
    print("{:s}".format(sorted(res)))
