#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Tests calculations for Pressure;  those in the Pressure subclass in speedcalc.py

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import unittest
import speedcalc
import test_logging

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

log = test_logging.TestLogging("ERROR")
sc_Pressure = speedcalc.Pressure()

# TODO: Make better method comments


class TestCalculations_pressure(unittest.TestCase):

    def test_vaporPressure_fromTemperature(self):
        """
        Is vapor pressure correctly calculated from degrees Celsius?
        """
        testName = "test_vaporPressure_fromTemperature"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            tenC = sc_Pressure.vapor_pressure_from_temperature(10.0)
            twentyC = sc_Pressure.vapor_pressure_from_temperature(20.0)
            thirtyC = sc_Pressure.vapor_pressure_from_temperature(30.0)
            negOneC = sc_Pressure.vapor_pressure_from_temperature(-1)

            self.assertEquals(round(tenC, 0), 1228.0)
            self.assertEquals(round(twentyC, 0), 2339.0)
            self.assertEquals(round(thirtyC, 0), 4244.0)
            self.assertEquals(round(negOneC, 2), 562.51)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_relativeHumidity(self):
        """
        Is saturation vapor pressure correctly calculated from degrees Celsius?
        """
        testName = "test_relativeHumidity"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            vaporPressure = 872.0
            saturationVaporPressure = 1228.0
            relativeHumidity = sc_Pressure.relative_humidity(vaporPressure, saturationVaporPressure)

            self.assertEquals(round(relativeHumidity, 2), 0.71)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_vaporPressure_fromRelativeHumidity(self):
        """
        Is saturation vapor pressure correctly calculated from degrees Celsius?
        """
        testName = "test_vaporPressure_fromRelativeHumidity"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            relativeHumidity = 0.71
            saturationVaporPressure = 1228.0
            vaporPressure = sc_Pressure.vapor_pressure_from_relative_humidity(relativeHumidity, saturationVaporPressure)

            self.assertEquals(round(vaporPressure, 2), 871.88)
            relativeHumidity = 71
            vaporPressure = sc_Pressure.vapor_pressure_from_relative_humidity(relativeHumidity, saturationVaporPressure)
            self.assertEquals(round(vaporPressure, 2), 871.88)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_vaporPressureDeficit(self):
        """
        Is the vapor pressure deficit correctly calculated?
        """
        testName = "test_vaporPressureDeficit"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            saturationVaporPressure = 1228.0
            vaporPressure = 872.0
            vaporPressureDeficit = sc_Pressure.vapor_pressure_deficit(saturationVaporPressure, vaporPressure)

            self.assertEquals(round(vaporPressureDeficit, 2), 356.00)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_pascalsTo_kiloPascals(self):
        """
        Conversion from Pascals to kiloPascals
        """
        testName = "test_pascalsTo_kiloPascals"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            Pressure1 = 1228.0
            Pressure2 = 872.0
            kPa1 = sc_Pressure.pascals_to_kilopascals(Pressure1)
            kPa2 = sc_Pressure.pascals_to_kilopascals(Pressure2)

            self.assertEquals(round(kPa1, 3), 1.228)
            self.assertEquals(round(kPa2, 3), 0.872)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_pascalsTo_hectoPascals(self):
        """
        Conversion from Pascals to hectoPascals
        """
        testName = "test_pascalsTo_hectoPascals"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            Pressure1 = 1228.0
            Pressure2 = 872.0
            hPa1 = sc_Pressure.pascals_to_hectopascals(Pressure1)
            hPa2 = sc_Pressure.pascals_to_hectopascals(Pressure2)

            self.assertEquals(round(hPa1, 3), 12.280)
            self.assertEquals(round(hPa2, 3), 8.720)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_dewPointTemperature(self):
        """
        Conversion from Pascals to hectoPascals
        """
        testName = "test_dewPointTemperature"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            vaporPressure = 1543  # RH = 0.66, satVaporPressure ~= 2339
            dewPointTemp = sc_Pressure.dew_point_temperature(vaporPressure)

            self.assertEquals(round(dewPointTemp, 3), 13.439)
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
    _suite.addTest(TestCalculations_pressure('test_vaporPressure_fromTemperature'))
    _suite.addTest(TestCalculations_pressure('test_relativeHumidity'))
    _suite.addTest(TestCalculations_pressure('test_vaporPressure_fromRelativeHumidity'))
    _suite.addTest(TestCalculations_pressure('test_vaporPressureDeficit'))
    _suite.addTest(TestCalculations_pressure('test_pascalsTo_kiloPascals'))
    _suite.addTest(TestCalculations_pressure('test_pascalsTo_hectoPascals'))
    _suite.addTest(TestCalculations_pressure('test_dewPointTemperature'))
    return _suite
