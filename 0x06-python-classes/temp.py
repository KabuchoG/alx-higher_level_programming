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
        def retres(self):
            """Returns the attribute"""
            return self.__size
        @retres.setter
        def retres(self, size):
            """Sets a value if certain conditions are met"""
            if type(size) != "int":
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
