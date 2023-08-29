#!/usr/bin/python3
"""
    This module seperates lines based on the delimeters '.', '?' and ':'
"""


def text_indentation(text):
    """
        A function that splits texts based on the delimeters ".?:"

        Args:
            text (str): string to be seperated

        Returns:
            None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    line = ""
    delimeters = ['.', ':', '?']
    for char in text:
        line += char
        if char in delimeters:
            lines.append(line.strip())
            lines.append("")
            line = ""

    if line:
        lines.append(line.strip())

    print('\n'.join(lines), end="")
