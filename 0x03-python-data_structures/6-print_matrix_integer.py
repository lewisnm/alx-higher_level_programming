#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            print(" ".join("{:d}".format(element) for element in row))
