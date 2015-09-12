# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 18:47:31 2015

@author: Ryan Dammrose aka MapLion
"""

import unittest
import speedcalc
import testLogging

log = testLogging.TestLogging()
con_Time = speedcalc.Time()


class TestCalculations_time(unittest.TestCase):

    def test_secondToMinute(self):
        """
        Are seconds correctly converted to minutes?
        """
        testName = "test_secondToMinute"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            seconds = 60
            minutes = con_Time.secondToMinute(seconds)
            self.assertEquals(minutes, 1)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_minuteToSecond(self):
        """
        Are minutes correctly converted to seconds?
        """
        testName = "test_minuteToSecond"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            minutes = 1
            seconds = con_Time.minuteToSecond(minutes)
            self.assertEquals(seconds, 60)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_minuteToHour(self):
        """
        Are minutes correctly converted to hours?
        """
        testName = "test_minuteToHour"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            minutes = 60
            hours = con_Time.minuteToHour(minutes)
            self.assertEquals(hours, 1)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_hourToMinute(self):
        """
        Are hours correctly converted to minutes?
        """
        testName = "test_hourToMinute"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            hours = 1
            minutes = con_Time.hourToMinute(hours)
            self.assertEquals(minutes, 60)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_secondToHour(self):
        """
        Are seconds correctly converted to hours?
        """
        testName = "test_secondToHour"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            seconds = 3600
            hours = con_Time.secondToHour(seconds)
            self.assertEquals(hours, 1)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_hourToSecond(self):
        """
        Are hours correctly converted to seconds?
        """
        testName = "test_hourToSecond"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            hours = 1
            seconds = con_Time.hourToSecond(hours)
            self.assertEquals(seconds, 3600)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_secondToDay(self):
        """
        Are hours correctly converted to seconds?
        """
        testName = "test_secondToDay"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            seconds = 86400
            days = con_Time.secondToDay(seconds)
            self.assertEquals(days, 1)
            # ------------------------------------
            log.printTestSuccess(testName)
        except:
            log.printTestFailure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_dayToSecond(self):
        """
        Are hours correctly converted to seconds?
        """
        testName = "test_dayToSecond"
        try:
            log.printTestBegin(testName)
            # ------------------------------------
            days = 1
            seconds = con_Time.dayToSecond(days)
            self.assertEquals(seconds, 86400)
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
    _suite.addTest(TestCalculations_time('test_secondToMinute'))
    _suite.addTest(TestCalculations_time('test_minuteToSecond'))
    _suite.addTest(TestCalculations_time('test_minuteToHour'))
    _suite.addTest(TestCalculations_time('test_hourToMinute'))
    _suite.addTest(TestCalculations_time('test_secondToHour'))
    _suite.addTest(TestCalculations_time('test_hourToSecond'))
    _suite.addTest(TestCalculations_time('test_secondToDay'))
    _suite.addTest(TestCalculations_time('test_dayToSecond'))
    return _suite
