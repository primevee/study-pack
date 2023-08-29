#!/usr/bin/python3
"""
 A module that retrieves class attributes
"""


class Student:
    """
        A class for a student object
    """

    def __init__(self, first_name, last_name, age):
        """
            class initialisation

            Args:
                first_name (str): first name
                last_name (str): last name
                age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            A method that that gets instances
        """

        result = {}

        for attr, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                result[attr] = value

        return result
