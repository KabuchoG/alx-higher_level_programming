#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add
my_list = [1, 2, 4, 1, 4, 2, 5, 6, 6, 8]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
