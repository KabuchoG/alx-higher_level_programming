#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    res = []
    for i, j in a_dictionary.items():
        res.append(j)
    res.sort()
    re = res.pop()
    for i, j in a_dictionary.items():
        if j == re:
            return i
