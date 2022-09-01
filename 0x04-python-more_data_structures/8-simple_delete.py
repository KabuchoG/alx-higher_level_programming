#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key != "":
        del a_dictionary[key]
    else:
        pass
    return a_dictionary
