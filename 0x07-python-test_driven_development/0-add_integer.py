#!/usr/bin/python3
"""
the module will be tested in txt file
"""
def add_integer(a, b=98):
   """
   Adds an iteger.
   """
   if type(a) is not int and type(a) is not float:
       raise TypeError("a must be an integer")
   if type(b) is not int and type(b) is not float:
       raise TypeError("b must be an integer")
   a = int(a)
   b = int(b)
   return a + b
if __name__ == "__main__":
    print(add_integer(30, 20))
