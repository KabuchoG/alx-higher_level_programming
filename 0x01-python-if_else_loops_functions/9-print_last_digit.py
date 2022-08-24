#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number = str(number)
        val = int(number[-1])
        return val
    else:
        number = str(number)
        val = int(number[-1]) * -1
        return val
