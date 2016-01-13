#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Runs all unittest suites

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import unittest
from testcalculations import time
from testcalculations import polygon
from testcalculations import ET
from testcalculations import length
from testcalculations import pressure

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

time_suite = time.suite()
length_suite = length.suite()
ET_suite = ET.suite()
pressure_suite = pressure.suite()
polygon_suite = polygon.suite()

"""
Run Tests

Note: Currently, the logging parameters "DEBUG", "WARNING" and "ERROR"
are set by the instantiation of testLogging.TestLogging()
of the first suite within the list.
"""
allTests = unittest.TestSuite((time_suite, length_suite, ET_suite, pressure_suite, polygon_suite))
runner = unittest.TextTestRunner()
runner.run(allTests)
