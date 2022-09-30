#!/usr/bin/python3
""" Class Rectangle inherits from Base
"""
from base import Base


class Rectangle(Base):
    """A rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instance object initializer"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""

        return self.__width

    @property
    def height(self):
        """Gets the height"""

        return self.__height

    @property
    def x(self):
        """Gets the x"""

        return self.__x

    @property
    def y(self):
        """Gets the y"""

        return self.__y

    @width.setter
    def width(self, value):
        """ sets the width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, hei):
        """ sets the height"""

        if type(hei) is not int:
            raise TypeError("height must be an integer")
        if hei <= 0:
            raise ValueError("height must be > 0")
        self.__height = hei

    @x.setter
    def x(self, value):
        """ sets the x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ sets the x"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        space = 0
        if self.__x >= self.__y:
            space = self.__x
        if self.__y >= self.__x:
            space = self.__y
        for step in range(self.__height):
            print("{}".format(space * " "), end='')
            for row in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Overrides str to print a specific string representation of the objct
        """

        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """assigns an argument to each attribute:
1st argument should be the id attribute
2nd argument should be the width attribute
3rd argument should be the height attribute
4th argument should be the x attribute
5th argument should be the y attribute
"""
        i = -1
        args = list(args)
        arg = [id, self.__width, self.__height, self.__x, self.__y]
        for ag in args:
            i += 1
            arg[i] = ag