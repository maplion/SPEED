#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 02: "Hello, World"

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

from __future__ import print_function  # Import to demonstrate Python 3 Print Function

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

name = "Ryan"
characteristic = "the MapLion"
print("Hello World!")
print("I am", end=" ")  # Demonstration of newline suppression in Python 3 print function
print("{0} {1}!".format(name, characteristic))

# print "Incidentally",
# print "This is how",
# print "we do it.",
# print "in Python 2.7.x (commas at end of line)",
# print "[i.e. suppress the newline]"
