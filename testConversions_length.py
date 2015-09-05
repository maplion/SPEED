# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 18:47:31 2015

@author: Ryan Dammrose aka MapLion
"""

import unittest
import convert
import testLogging

log = testLogging.TestLogging()
con_Length = convert.Length()

class TestConversions_length(unittest.TestCase):

    def meterToMillimeter(self):
        """
        Is Energy flux correctly converting to the amount of Water Evaporated?
        """
        testName = "meterToMillimeter"
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
    _suite.addTest(TestConversions_length('meterToMillimeter'))
    return _suite

