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

    def __str__(self):
        """
            A method for str

            Returns:
                str: A string representaing of a parimeter

        """
        self.prem = ""
        for _ in range(self.height):
            self.prem += "#" * self.width + '\n'
        return self.prem.strip()

    def __repr__(self):
        """
            A method that prints a string representation of instances

            Returns:
                str: string representation of instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

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

    def area(self):
        """
            Area method that returns the area

            Returns:
                int: width * height
        """

        return self.width * self.height

    def perimeter(self):
        """
            Area method that returns perimeter

            Returns:
                int: 2 * (height + width)
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
