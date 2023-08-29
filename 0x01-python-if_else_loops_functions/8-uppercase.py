#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            string += "{:c}".format(ord(i) - 32)
        else:
            string += "{:c}".format(ord(i))
    print("{}".format(string))
