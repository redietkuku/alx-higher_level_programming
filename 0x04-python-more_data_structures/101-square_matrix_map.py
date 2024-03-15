#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda rows: list(map((lambda i: i * i), rows))), matrix))
