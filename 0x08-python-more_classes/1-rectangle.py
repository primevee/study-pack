#!/usr/bin/python3
"""
    This is a empty class called rectangle
"""


class Rectangle:
    """
        This is an empty class
    """

    def __init__(self, width=0, height=0):
        """
            Initializes a rectangle instance

            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """
            Getter method for width of rectangle

            Returns:
                int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter for width of rectangle

            Args:
                value (int): width of rectangle

            Raises:
                TypeError: If value is not integer
                ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Getter method for height of rectangle

            Returns:
                int: Value of height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter method for height of a rectangle

            Args:
                value (int): height of rectangle

            Raises:
                TypeError: If value is not integer
                ValueError: If value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
