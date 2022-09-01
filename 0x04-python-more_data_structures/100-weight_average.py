#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0
    we = 0
    for i in my_list:
        res += + (i[0] * i[1])
        we += + i[1]
    return res / we
