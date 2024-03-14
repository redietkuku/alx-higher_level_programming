#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()

    for x in range(len(matrix)):
        new[x] = list(map(lambda x: x**2, matrix[x]))

    return (new)
