#!/usr/bin/python3
"""
    A module that sets an attribute to a class
"""


def add_attribute(obj, name, attribute):
    """
        A function that sets an attribute to a class

        Args:
            obj (class): The class
            name (str): the attribute name
            attribute: the attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add attribute")
    setattr(obj, name, attribute)
