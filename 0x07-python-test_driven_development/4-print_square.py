#!/usr/bin/python3
def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is not int:
        raise TypeError("size must be an integer")
    for i in range(size):
        for n in range(size):
            print("#", end='')
        print()
if __name__ == "__main__":
    print_square(10)
    print_square('h')
    print_square(1.5)
