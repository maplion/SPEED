# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 18:47:31 2015

@author: Ryan Dammrose aka MapLion
"""

import logging

class TestLogging(object):

    def __init__(self, logLevel="WARNING"):
        """
        TestLogging Constructor
        @param logLevel: the level of logging that one wants to see in the tests

        Sets level of logging; defaults to logging.WARNING to suppress successes.
        Set level of logging to logging.DEBUG to see all tests.
        """
        self._level = logLevel
        if self._level == "DEBUG":
            logging.basicConfig(level=logging.DEBUG)
        elif self._level == "ERROR":
            logging.basicConfig(level=logging.ERROR)
        else:
            logging.basicConfig(level=logging.WARNING)

    def printTestBegin(self, testName):
        """
        @param testName: Name of test being run

        Prints a line before test assertions so one knows the test is running.
        """
        self._testName = testName
        log = logging.getLogger(self._testName)
        log.debug("...")

    def printTestSuccess(self, testName):
        """
        @param testName: Name of test being run

        Prints a line for success if the test succeeds.
        """
        self._testName = testName
        log = logging.getLogger(self._testName)
        log.debug("Success\n")

    def printTestFailure(self, testName):
        """
        @param testName: Name of test being run

        Prints a line for failure if the test fails.
        """
        self._testName = testName
        log = logging.getLogger(self._testName)
        if self._level == "ERROR":
            log.exception("FAILURE\n")
        else:
            log.warning("FAILURE\n")

    def printTestFailureException(self, testName):
        """
        @param testName: Name of test being run

        Prints an exception block for failure if the test fails.
        """
        self._testName = testName
        log = logging.getLogger(self._testName)
        log.exception("FAILURE\n")