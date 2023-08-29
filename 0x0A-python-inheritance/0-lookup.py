#!/usr/bin/python3
"""
    A module that returns the list of all available
    * Attributes
    * methods
"""


def lookup(obj):
    """
        A funtion that return the attributes of a function.

        Args:
        obj (class): a class object

        Returns: a dictionary of all attributes
    """
    return dir(obj)
