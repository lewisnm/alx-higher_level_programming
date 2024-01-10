#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
   squared = [[item ** 2 for item in row]for row in matrix]
   return squared
