#!/usr/bin/python3
"""
    my int module it changes == to != and vice versa
"""


class MyInt(int):
    """
        A lass that inherits the int class

        Args:
            int (class): the int inherited class
    """

    def __eq__(self, other):
        """
            A method that changes == to !=
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
            A method that changes != to ==
        """

        return super().__eq__(other)
