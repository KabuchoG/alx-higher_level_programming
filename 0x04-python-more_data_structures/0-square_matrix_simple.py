#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = [(x ** 2) for i in matrix for x in i]
    return res
