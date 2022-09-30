#!/usr/bin/python3
""" The base class"""


class Base:
    """ The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The instance object initializer"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
