#!/usr/bin/python3
"""
    A module that saves a string json representation of an object
"""


import json


def save_to_json_file(my_obj, filename):
    """
        A function that prints json representation of object

        Args:
            my_obj (class): A class object
            filename (str): The filename
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
