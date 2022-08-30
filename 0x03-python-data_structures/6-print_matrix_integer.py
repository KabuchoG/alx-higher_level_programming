#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        new = matrix[i]
        for n in range(len(new)):
            if n != 0:
                print(' ', end='')
            print("{:d}".format(new[n]), end='')
        print()
