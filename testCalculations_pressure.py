# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 18:47:31 2015

@author: Ryan Dammrose aka MapLion
"""

import unittest
import speedcalc
import testLogging

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
            twentyC_kpa = sc_Pressure.saturationVaporPressure(20, resultPascal="kpa")
            thirtyC_hpa = sc_Pressure.saturationVaporPressure(30, resultPascal="hpa")

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

