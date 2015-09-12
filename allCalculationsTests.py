#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Runs all unittest suites

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import unittest
import testCalculations_time
import testCalculations_length
import testCalculations_ET
import testCalculations_pressure

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

time_suite = testCalculations_time.suite()
length_suite = testCalculations_length.suite()
ET_suite = testCalculations_ET.suite()
pressure_suite = testCalculations_pressure.suite()

"""
Run Tests

Note: Currently, the logging parameters "DEBUG", "WARNING" and "ERROR"
are set by the instantiation of testLogging.TestLogging()
of the first suite within the list.
"""
allTests = unittest.TestSuite((time_suite, length_suite, ET_suite, pressure_suite))
runner = unittest.TextTestRunner()
runner.run(allTests)
