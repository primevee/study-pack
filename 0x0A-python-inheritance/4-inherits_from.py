#!/usr/bin/python3
"""
A module that checks if a class instance is a subclass
"""


def inherits_from(obj, a_class):
    """
        checks if obj is a subclass

        Args:
            obj (class): class object
            a_class: class to be tested

        Returns:
            True if obj is a subclass of a_class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
