#!/usr/bin/python3
"""
    A module that adds all arguments to a python list
"""

import sys
import json


sv_to_json = __import__('5-save_to_json_file').save_to_json_file
ld_from_json = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
        A module that adds all arguments to a python list
    """

    filename = "add_item.json"
    try:
        my_list = ld_from_json(filename)
    except FileNotFoundError:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    sv_to_json(my_list, filename)


add_items()
