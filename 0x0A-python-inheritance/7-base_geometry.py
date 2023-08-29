#!/usr/bin/python3
"""
    A module that executes geometric functions
"""


class BaseGeometry:
    """
        An empty class
    """

    def area(self):
        """
            this method raises an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A method that validates that a value is an int

            Args:
                name (str): The name
                value (int): the value

            Raises:
                TypeError: if value is not int
                ValueError: if value is <= 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
