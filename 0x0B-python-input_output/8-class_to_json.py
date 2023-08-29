#!/usr/bin/python3
"""
    A module that adds attributes to dict
"""


def class_to_json(obj):
    """
        A module that adds attributes to dict

        Args:
            obj (class): class object

    """

    if hasattr(obj, "__dict__"):
        result = {}

        for attr, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                result[attr] = value

        return result
