#!/usr/bin/python3
"""
This module defines a rectangle and its width
"""


class Rectangle:
    """ A class with widh of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        a reference to the instance itself
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        get the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting a value
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting a value
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Returns a printable representation of the class"""

        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        string += "\n".join("#" * self.__width for j in range(self.__height))
        return string
