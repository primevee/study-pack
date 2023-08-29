#!/usr/bin/python3
"""
    A module that reads a file
"""


def read_file(filename=""):
    """
        A funtion that reads a file.

        Args:
            filename (str): The filename
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
