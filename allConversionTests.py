# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 18:47:31 2015

@author: Ryan Dammrose aka MapLion
"""
import unittest
import testConversions_time
import testConversions_length
import testConversions_ET


time_suite = testConversions_time.suite()
length_suite = testConversions_length.suite()
ET_suite = testConversions_ET.suite()

# Run Tests
allTests = unittest.TestSuite((time_suite, length_suite, ET_suite))
runner = unittest.TextTestRunner()
runner.run(allTests)