#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Tests calculations for length; those in the Length subclass in speedcalc.py

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import unittest
import speedcalc
import test_logging

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

log = test_logging.TestLogging()
sc_Length = speedcalc.Length()


class TestCalculations_length(unittest.TestCase):

    def meterToMillimeter(self):
        """
        Are meters correctly converted to millimeters?
        """
        testName = "meter_to_millimeter"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            meters = 1
            millimeters = sc_Length.meter_to_millimeter(meters)
            self.assertEquals(millimeters, 1000)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def millimeterToMeter(self):
        """
        Are millimeters correctly converted to meters?
        """
        testName = "millimeter_to_meter"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            millimeters = 1000
            meters = sc_Length.millimeter_to_meter(millimeters)
            self.assertEquals(meters, 1)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")
##########################################################################################


def suite():
    """
    Gather all the tests from this module in a test suite.
    """
    _suite = unittest.TestSuite()
    _suite.addTest(TestCalculations_length('meter_to_millimeter'))
    _suite.addTest(TestCalculations_length('millimeter_to_meter'))
    return _suite
