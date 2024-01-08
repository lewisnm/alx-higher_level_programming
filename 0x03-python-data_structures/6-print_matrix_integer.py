#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            elements = 0
            for element in row:
                print("{:d}".format(element), end=" ")
                elements += 1

                if elements == 3:
                    print()
                    elements = 0

