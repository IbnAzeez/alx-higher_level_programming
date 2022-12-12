#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    for row in range(len(matrix_copy)):
        matrix_copy[row] = list(map(lambda x: x ** 2, matrix_copy[row]))
    return mattix_copy
