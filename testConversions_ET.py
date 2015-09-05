# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 18:47:31 2015

@author: Ryan Dammrose aka MapLion
"""

import unittest
import convert
import testLogging

log = testLogging.TestLogging()
con_ET = convert.ET()

class TestConversions_ET(unittest.TestCase):

    def test_energyFluxToWaterEvaporated(self):
        """
        Is Energy flux correctly converting to the amount of Water Evaporated?
        """
        testName = "test_energyFluxToWaterEvaporated"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            # ET_mf = 3.0e-5 # mass flux rate in kg/(m^2*s)
            # ET_mm_per_day = con_ET.energyFluxToWaterEvaporated(ET_mf)
            # self.assertEquals(ET_mm_per_day, 2.592000)
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
    _suite.addTest(TestConversions_ET('test_energyFluxToWaterEvaporated'))
    return _suite

