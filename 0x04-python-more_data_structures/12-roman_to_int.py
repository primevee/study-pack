#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'M': 1000}
    hold = 0
    total = 0
    if not roman_string or not type(roman_string) == str:
        return 0
    for char in reversed(roman_string):
        value = roman_num.get(char, 0)
        if value >= hold:
            total += value
        else:
            total -= value
        hold = value
    return total
