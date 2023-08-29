#!/usr/bin/python3
"""
    A module that takes a string representation and return an object
"""


import json


def from_json_string(my_str):
    """
        A function that returns a object loaded from json

        Args:
            my_str (str): A string re[resentation of a json object
    """

    return json.loads(my_str)
