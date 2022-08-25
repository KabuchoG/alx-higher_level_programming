#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    argl = len(arg)
    if argl == 1:
        print("0 arguments.")
    elif argl == 2:
        print("1 argument:")
        print("1: {}".format(arg[1]))
    else:
        print(f"{argl - 1} arguments:")
        for n in range(1, argl):
            print(f"{n}: {arg[n]}")
