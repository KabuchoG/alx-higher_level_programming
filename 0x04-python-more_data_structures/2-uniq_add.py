#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    res = []
    for i in range(len(my_list)):
        if my_list.count(my_list[i]) == 1:
            result += + my_list[i]
        else:
            if my_list[i] in res:
                pass
            else:
                res.append(my_list[i])
    for i in range(len(res)):
        result += + res[i]
    return result

