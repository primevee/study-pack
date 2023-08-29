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
        self.__size = 0
        self.size = size

    def area(self):
        """
            method the defines an area of a square

        """
        return self.__size ** 2

    @property
    def size(self):
        """
            method that returns private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            method that sets size

            Args:
                value (int): value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
            print square using #
        """

        if not self.__size:
            print()

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
