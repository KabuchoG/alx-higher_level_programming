#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    total = 0
    for n in range(1, len(arg)):
        num = int(arg[n])
        total += + num
    print(f"{total}")
