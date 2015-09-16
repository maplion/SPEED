#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Tests calculations for Pressure;  those in the Pressure subclass in speedcalc.py

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
sc_Pressure = speedcalc.Pressure()


class TestCalculations_pressure(unittest.TestCase):

    def test_saturationVaporPressure(self):
        """
        Is saturation vapor pressure correctly calculated from degrees Celsius?
        """
        testName = "test_saturationVaporPressure"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            tenC_pa = sc_Pressure.saturationVaporPressure(10)
            twentyC_kpa = sc_Pressure.saturationVaporPressure(20, units="kpa")
            thirtyC_hpa = sc_Pressure.saturationVaporPressure(30, units="hpa")

            self.assertEquals(round(tenC_pa, 0), 1228)
            self.assertEquals(round(twentyC_kpa, 3), 2.339)
            self.assertEquals(round(thirtyC_hpa, 2), 42.44)
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
    _suite.addTest(TestCalculations_pressure('test_saturationVaporPressure'))
    return _suite
