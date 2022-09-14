#!/usr/bin/python3
"""This is a class that defines a private attribute"""


class Square:
    """Attributes self is used to reference an insance to itself.
    size attribute is private and will fail toexcecute because there are no
    setters and getters"""
    def __init__(self, size):
        self.__size = size
