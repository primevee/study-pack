#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_av = len(sys.argv)
    if len_av > 1:
        if len_av == 2:
            print("1 argument:")
            print("{}: {}".format(len_av - 1, sys.argv[1]))
        else:
            print("{} arguments:".format(len_av - 1))
            for i in range(1, len_av):
                print("{}: {}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
