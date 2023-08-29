#!/usr/bin/python3

"""
    this module defines a square
"""


class Square:

    """
        this class represents a square

        Attributes:
            __size (int): size of a square
        Methods:
            No methods are defined in this class
    """

    def __init__(self, size=0):
        """
            Initialise an instance of this class

            Args:
                size (int): the size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            method the defines an area of a square

        """
        return self.__size ** 2
