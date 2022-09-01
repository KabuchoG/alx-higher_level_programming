#1/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.items():
        return a_dictionary
    for i, j in a_dictionary.items():
        if j == value:
            del i
    return a_dictionary
