#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    rev = my_list[::-1]
    for i in range(len(my_list)):
        print("{}".format(rev[i]))
