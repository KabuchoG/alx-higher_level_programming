#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        j = matrix[i]
        for n in range(len(j)):
            print("{:d} {}".format(j[n], ' '), end='')
        print()
