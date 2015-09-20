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

log = testLogging.TestLogging("ERROR")
sc_Pressure = speedcalc.Pressure()

# TODO: Make better method comments


class TestCalculations_pressure(unittest.TestCase):

    def test_vaporPressure_fromTemperature(self):
        """
        Is vapor pressure correctly calculated from degrees Celsius?
        """
        testName = "test_vaporPressure_fromTemperature"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            tenC_pa = sc_Pressure.vaporPressure_fromTemperature(10.0)
            sc_Pressure2 = speedcalc.Pressure(units="kpa")
            sc_Pressure3 = speedcalc.Pressure(units="hpa")
            twentyC_kpa = sc_Pressure2.vaporPressure_fromTemperature(20.0)
            thirtyC_hpa = sc_Pressure3.vaporPressure_fromTemperature(30.0)

            self.assertEquals(round(tenC_pa, 0), 1228.0)
            self.assertEquals(round(twentyC_kpa, 3), 2.339)
            self.assertEquals(round(thirtyC_hpa, 2), 42.44)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_relativeHumidity(self):
        """
        Is saturation vapor pressure correctly calculated from degrees Celsius?
        """
        testName = "test_relativeHumidity"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            vaporPressure = 872.0
            saturationVaporPressure = 1228.0
            relativeHumidity = sc_Pressure.relativeHumidity(vaporPressure, saturationVaporPressure)

            self.assertEquals(round(relativeHumidity, 2), 0.71)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_vaporPressure_fromRelativeHumidity(self):
        """
        Is saturation vapor pressure correctly calculated from degrees Celsius?
        """
        testName = "test_vaporPressure_fromRelativeHumidity"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            relativeHumidity = 0.71
            saturationVaporPressure = 1228.0
            vaporPressure = sc_Pressure.vaporPressure_fromRelativeHumidity(relativeHumidity, saturationVaporPressure)

            self.assertEquals(round(vaporPressure, 2), 871.88)
            relativeHumidity = 71
            vaporPressure = sc_Pressure.vaporPressure_fromRelativeHumidity(relativeHumidity, saturationVaporPressure)
            self.assertEquals(round(vaporPressure, 2), 871.88)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_vaporPressureDeficit(self):
        """
        Is the vapor pressure deficit correctly calculated?
        """
        testName = "test_vaporPressureDeficit"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            saturationVaporPressure = 1228.0
            vaporPressure = 872.0
            vaporPressureDeficit = sc_Pressure.vaporPressureDeficit(saturationVaporPressure, vaporPressure)

            self.assertEquals(round(vaporPressureDeficit, 2), 356.00)
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
    _suite.addTest(TestCalculations_pressure('test_vaporPressure_fromTemperature'))
    _suite.addTest(TestCalculations_pressure('test_relativeHumidity'))
    _suite.addTest(TestCalculations_pressure('test_vaporPressure_fromRelativeHumidity'))
    _suite.addTest(TestCalculations_pressure('test_vaporPressureDeficit'))
    return _suite
