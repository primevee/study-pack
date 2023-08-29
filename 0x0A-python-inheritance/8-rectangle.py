#!/usr/bin/python3
"""
    A module that holds the rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
        A class for a rectangle

        Args:
            BaseGeometry (class): BaseGeometry class
    """

    def __init__(self, width, height):
        """
            Initialising the class

            Args:
                width (int): width of triangle
                height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
