#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    div_res = 0
    result_list = []
    while i < list_length:
        try:
            div_res = my_list_1[i] / my_list_2[i]
            result_list.append(div_res)
        except TypeError:
            print("wrong type")
            result_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            i += 1
    return result_list
