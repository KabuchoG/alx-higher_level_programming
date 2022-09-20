#!/usr/bin/python3
"""Testing a function cases
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMax(unittest.TestCase):
    """
    Testing class
    """
    def test_max_integer(self):
        """
        Testing method
        """
        a = [1,3,5,7]
        b = []
        c = [2,2,2,2,2]
        self.assertEqual(max_integer(a), 7)
        self.assertEqual(max_integer(b), None)
        self.assertEqual(max_integer(c), 2)

