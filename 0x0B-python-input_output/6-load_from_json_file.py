#!/usr/bin/python3
"""
    A module that reads a json file
"""


import json


def load_from_json_file(filename):
    """
        A function that reads a json file

        Args:
            filename (str): filename
    """

    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
