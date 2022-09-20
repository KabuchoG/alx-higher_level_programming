#!/usr/bin/python3
"""
The mode will be tested
"""
def matrix_divided(matrix, div):
    """ 
    A division function given different conditions
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    mat = matrix.copy()
    length = len(mat[0])
    for i in range(len(mat)):
        if len(mat[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        for n in range(len(mat[i])):
            act = mat[i]
            if type(act[n]) is not int and type(act[n]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            mat[i][n] = round(act[n] / div, 2)
    return mat
if __name__ == "__main__":
    matrix = [[1,2,3,4], [1,2,3,4], [1,2,3,4,]]
    print(matrix_divided(matrix, 3))
