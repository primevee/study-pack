#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    else:
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
        return my_list[-1]
