#!/usr/bin/python3
def islower(c):
    for n in c:
        if (ord(n) > 96 and ord(n) < 123):
            return True
        else:
            return False
