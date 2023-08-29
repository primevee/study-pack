#!/usr/bin/python3
"""
 A function that returns a json representation
"""


import json


def to_json_string(my_obj):
    """
        A function that returns a json representation

        Args:
            my_obj (class): An object
    """

    return json.dumps(my_obj)
