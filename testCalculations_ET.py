#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Tests calculations for evapotranspiration calculations; those in the ET subclass in speedcalc.py

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
sc_ET = speedcalc.ET()


class TestCalculations_ET(unittest.TestCase):

    def test_massFluxToWaterEvaporated(self):
        """
        Is mass flux correctly converting to the amount of Water Evaporated?
        """
        testName = "test_massFluxToWaterEvaporated"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            ET_mf = 3.0e-5  # mass flux rate in kg/(m^2*s)
            ET_mm_per_day = sc_ET.massFluxToWaterEvaporated(ET_mf)
            self.assertEquals(round(ET_mm_per_day, 6), 2.592000)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_energyFluxToWaterEvaporated(self):
        """
        Is Energy flux correctly converting to the amount of Water Evaporated?
        """
        testName = "test_energyFluxToWaterEvaporated"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            ET_ef = 30  # energy flux rate in W/m^2
            ET_ef_2 = 100  # energy flux rate in W/m^2
            ET_mm_per_day = sc_ET.energyFluxToWaterEvaporated(ET_ef)
            ET_mm_per_day_2 = sc_ET.energyFluxToWaterEvaporated(ET_ef_2)
            self.assertEquals(round(ET_mm_per_day, 2), 1.15)
            self.assertEquals(round(ET_mm_per_day_2, 2), 3.82)
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
    _suite.addTest(TestCalculations_ET('test_massFluxToWaterEvaporated'))
    _suite.addTest(TestCalculations_ET('test_energyFluxToWaterEvaporated'))
    return _suite
