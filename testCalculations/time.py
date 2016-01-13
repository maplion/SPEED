#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Tests calculations for Time; those in the Time subclass in speedcalc.py

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import unittest
import speedcalc
import test_logging

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

log = test_logging.TestLogging()
con_Time = speedcalc.Time()


class TestCalculations_time(unittest.TestCase):

    def test_secondToMinute(self):
        """
        Are seconds correctly converted to minutes?
        """
        testName = "test_secondToMinute"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            seconds = 60
            minutes = con_Time.second_to_minute(seconds)
            self.assertEquals(minutes, 1)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_minuteToSecond(self):
        """
        Are minutes correctly converted to seconds?
        """
        testName = "test_minuteToSecond"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            minutes = 1
            seconds = con_Time.minute_to_second(minutes)
            self.assertEquals(seconds, 60)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_minuteToHour(self):
        """
        Are minutes correctly converted to hours?
        """
        testName = "test_minuteToHour"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            minutes = 60
            hours = con_Time.minute_to_hour(minutes)
            self.assertEquals(hours, 1)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_hourToMinute(self):
        """
        Are hours correctly converted to minutes?
        """
        testName = "test_hourToMinute"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            hours = 1
            minutes = con_Time.hour_to_minute(hours)
            self.assertEquals(minutes, 60)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_secondToHour(self):
        """
        Are seconds correctly converted to hours?
        """
        testName = "test_secondToHour"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            seconds = 3600
            hours = con_Time.second_to_hour(seconds)
            self.assertEquals(hours, 1)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_hourToSecond(self):
        """
        Are hours correctly converted to seconds?
        """
        testName = "test_hourToSecond"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            hours = 1
            seconds = con_Time.hour_to_second(hours)
            self.assertEquals(seconds, 3600)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_secondToDay(self):
        """
        Are hours correctly converted to seconds?
        """
        testName = "test_secondToDay"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            seconds = 86400
            days = con_Time.second_to_day(seconds)
            self.assertEquals(days, 1)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_dayToSecond(self):
        """
        Are hours correctly converted to seconds?
        """
        testName = "test_dayToSecond"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            days = 1
            seconds = con_Time.day_to_second(days)
            self.assertEquals(seconds, 86400)
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
    _suite.addTest(TestCalculations_time('test_secondToMinute'))
    _suite.addTest(TestCalculations_time('test_minuteToSecond'))
    _suite.addTest(TestCalculations_time('test_minuteToHour'))
    _suite.addTest(TestCalculations_time('test_hourToMinute'))
    _suite.addTest(TestCalculations_time('test_secondToHour'))
    _suite.addTest(TestCalculations_time('test_hourToSecond'))
    _suite.addTest(TestCalculations_time('test_secondToDay'))
    _suite.addTest(TestCalculations_time('test_dayToSecond'))
    return _suite
