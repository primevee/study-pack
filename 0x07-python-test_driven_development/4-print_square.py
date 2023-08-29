#!/usr/bin/python3
"""
    This module prints a square using #
"""


def print_square(size):
    """
        a function that prints a square

        Args:
            size (int): size of triangle

        Returns:
            None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)
