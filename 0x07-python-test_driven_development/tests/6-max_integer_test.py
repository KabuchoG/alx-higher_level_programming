#!/usr/bin/python3
"""Testing a function cases"""
import unittest
from 6-max_integer import max_integer
class TestMax(unittest.TestCase):
    def testmax(self):
        self.assertEqual(max_integer([1,3,5,7]), 7)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2,2,2,2]), 2)

