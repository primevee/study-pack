#!/usr/bin/python3
"""
    A module that returns a bool:
    * True if object matches the instance
    * False otherwise
"""


def is_same_class(obj, a_class):
    """
        A function that checks if object matches instance

        Args:
            obj (class): The object
            a_class: the instance

        Returns: True if object matches instance false otherwise
    """

    return type(obj) is a_class
