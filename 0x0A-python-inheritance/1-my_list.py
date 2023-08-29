#!/usr/bin/python3
"""
A module tha inherits the class list as a super class
"""


class MyList(list):
    """
        A class that inherits the list class
    """

    def print_sorted(self):
        """
            print the list.
        """

        print(sorted(self))
