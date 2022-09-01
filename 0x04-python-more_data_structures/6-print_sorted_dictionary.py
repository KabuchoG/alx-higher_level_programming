#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = (a_dictionary.keys()).sort()
    for i in res:
        print("{:s} : {}".format(i, a_dictionary.get(i)))
