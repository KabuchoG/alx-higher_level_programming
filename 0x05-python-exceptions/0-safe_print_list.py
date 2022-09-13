#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0;
    try:
        for n in  range(x):
            num += 1
            print(my_list[n], end='')
    except:
        print()
        return (num - 1)
    else:
        print()
        return num
