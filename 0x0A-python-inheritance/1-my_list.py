#!/usr/bin/python3
"""
Contains class MyList
"""


class MyList(list):
    """
    Returns a sorted list"""

    def print_sorted(self):
        return self.sort()
