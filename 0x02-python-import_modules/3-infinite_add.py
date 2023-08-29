#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_av = len(sys.argv)
    number = 0
    if len_av > 1:
        for i in range(1, len_av):
            number += int(sys.argv[i])
    print(number)
