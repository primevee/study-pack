#!/usr/bin/python3
"""
    A module that holds the rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
        A class for a rectangle

        Args:
            BaseGeometry (class): BaseGeometry class
    """

    def __init__(self, size):
        """
            Initialising the class

            Args:
                size (int): size of triangle
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            a method that returns the area
        """
        return self.__size * self.__size

    def __str__(self):
        """
            str special method
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
