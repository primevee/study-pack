#!/usr/bin/python3

"""
This module adds two number that are integers r float type
"""

def add_integer(a, b=98):
    """
        A function that adds two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + (b)

