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

    def test_energyFlux_to_waterEvaporated(self):
        """
        Is Energy flux correctly converting to the amount of Water Evaporated?
        """
        testName = "test_energyFlux_to_waterEvaporated"
        try:
            log.printTestBegin(testName)
            # ------------------------------------

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
    _suite.addTest(TestConversions_ET('test_energyFlux_to_waterEvaporated'))
    return _suite

