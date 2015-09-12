#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Tests calculations for length; those in the Length subclass in speedcalc.py

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import unittest
import speedcalc
import testLogging

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

log = testLogging.TestLogging()
sc_Length = speedcalc.Length()


class TestCalculations_length(unittest.TestCase):

    def meterToMillimeter(self):
        """
        Are meters correctly converted to millimeters?
        """
        testName = "meterToMillimeter"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            meters = 1
            millimeters = sc_Length.meterToMillimeter(meters)
            self.assertEquals(millimeters, 1000)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def millimeterToMeter(self):
        """
        Are millimeters correctly converted to meters?
        """
        testName = "millimeterToMeter"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            millimeters = 1000
            meters = sc_Length.millimeterToMeter(millimeters)
            self.assertEquals(meters, 1)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")
##########################################################################################


def suite():
    """
    Gather all the tests from this module in a test suite.
    """
    _suite = unittest.TestSuite()
    _suite.addTest(TestCalculations_length('meterToMillimeter'))
    _suite.addTest(TestCalculations_length('millimeterToMeter'))
    return _suite
