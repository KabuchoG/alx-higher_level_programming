#!/usr/bin/python3
""" Class Rectangle inherits from Base
"""
from base import Base


class Rectangle(Base):
    """A rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instance object initializer"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""

        return self.__width

    @width.setter
    def width(self, width):
        """ sets the width"""

        if type(width) is not int:
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be > 0".format(width))
        self.__width = width

    @property
    def height(self):
        """Gets the height"""

        return self.__height

    @height.setter
    def height(self, height):
        """ sets the height"""

        if type(height) is not int:
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be > 0".format(height))
        self.__height = height

    @property
    def x_g(self):
        """Gets the x"""

        return self.__x

    @x_g.setter
    def x_g(self, x):
        """ sets the x"""

        if type(x) is not int:
            raise TypeError("{} must be an integer".format(x))
        if x < 0:
            raise ValueError("{} must be >= 0".format(x))
        self.__x = x

    @property
    def y_g(self):
        """Gets the y"""

        return self.__y

    @y_g.setter
    def y_g(self, y):
        """ sets the x"""

        if type(y) is not int:
            raise TypeError("{} must be an integer".format(y))
        if y < 0:
            raise ValueError("{} must be >= 0".format(y))
        self.__y = y