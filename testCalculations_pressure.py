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
            tenC = sc_Pressure.vaporPressure_fromTemperature(10.0)
            twentyC = sc_Pressure.vaporPressure_fromTemperature(20.0)
            thirtyC = sc_Pressure.vaporPressure_fromTemperature(30.0)
            negOneC = sc_Pressure.vaporPressure_fromTemperature(-1)

            self.assertEquals(round(tenC, 0), 1228.0)
            self.assertEquals(round(twentyC, 0), 2339.0)
            self.assertEquals(round(thirtyC, 0), 4244.0)
            self.assertEquals(round(negOneC, 2), 562.51)
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

    def test_pascalsTo_kiloPascals(self):
        """
        Conversion from Pascals to kiloPascals
        """
        testName = "test_pascalsTo_kiloPascals"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            Pressure1 = 1228.0
            Pressure2 = 872.0
            kPa1 = sc_Pressure.pascalsTo_kiloPascals(Pressure1)
            kPa2 = sc_Pressure.pascalsTo_kiloPascals(Pressure2)

            self.assertEquals(round(kPa1, 3), 1.228)
            self.assertEquals(round(kPa2, 3), 0.872)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_pascalsTo_hectoPascals(self):
        """
        Conversion from Pascals to hectoPascals
        """
        testName = "test_pascalsTo_hectoPascals"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            Pressure1 = 1228.0
            Pressure2 = 872.0
            hPa1 = sc_Pressure.pascalsTo_hectoPascals(Pressure1)
            hPa2 = sc_Pressure.pascalsTo_hectoPascals(Pressure2)

            self.assertEquals(round(hPa1, 3), 12.280)
            self.assertEquals(round(hPa2, 3), 8.720)
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
    _suite.addTest(TestCalculations_pressure('test_pascalsTo_kiloPascals'))
    _suite.addTest(TestCalculations_pressure('test_pascalsTo_hectoPascals'))
    return _suite
