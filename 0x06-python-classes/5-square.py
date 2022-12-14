#!/usr/bin/python3
"""This is a class that defines a private attribute"""


class Square:
    """Attributes self is used to reference an insance to itself.
    size attribute is private and will fail toexcecute because there are no
    setters and getters"""
    def __init__(self, size=0):
        """inititalizes each time an instance is created"""
        self.__size = size

    @property
    def size(self):
        """This is a setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter, sets a value"""
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area"""
        return self.__size ** 2

    def my_print(self):
        """"Print in stdout"""
        if self.__size == 0:
            print()
        else:
            for n in range(self.__size):
                for r in range(self.__size):
                    print("#", end='')
                print()
