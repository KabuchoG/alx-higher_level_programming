#!/usr/bin/python3
""" Class Square
"""
from rectangle import Rectangle


class Square(Rectangle):
    """square inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialising the square"""

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Overrides str to print a specific string representation of the object
                """

        return "[{}] ({}) {}/{} - {}".format(__class__.__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Gets the size"""

        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns variable attributes and key word attributes
        """

        i = -1
        # arg = [id, self.__width, self.__height, self.__x, self.__y]
        if len(args) != 0:
            for ag in args:
                i += 1
                if i == 0:
                    self.id = ag
                if i == 1:
                    self.size = ag
                if i == 2:
                    self.x = ag
                if i == 3:
                    self.y = ag
        else:
            for att, val in kwargs.items():
                if att == 'id':
                    self.id = val
                if att == 'size':
                    self.size = val
                if att == 'x':
                    self.x = val
                if att == 'y':
                    self.y = val

    def to_dictionary(self):
        """ Returns a dictionary representation of the square
        """

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
