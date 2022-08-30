#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            for n in range(len(my_list)):
                if my_list[i] < my_list[n]:
                    temp = my_list[i]
                    my_list[i] = my_list[n]
                    my_list[n] = temp
        my_list.reverse()
        return my_list[0]
