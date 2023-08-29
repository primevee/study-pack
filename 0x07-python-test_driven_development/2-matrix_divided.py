#!/usr/bin/python3
"""
    This module devides a matrix by the value div
"""


def matrix_divided(matrix, div):
    """
        A function that divides a matrix with div

        Args:
            matrix (list of lists): A matrix of integers
            div (int or float): The number to divide by

        Returns:
            a matrix that is divided by div
    """

    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    for row in matrix:
        for i in range(len(row)):
            if not isinstance(row[i], (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
                            of integers/floats"
                        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []

    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
