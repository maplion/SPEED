#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for logging tests and verbose logging

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import logging

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"


class TestLogging(object):

    def __init__(self, log_level="WARNING"):
        """
        TestLogging Constructor
        @param log_level: the level of logging that one wants to see in the tests

        Sets level of logging; defaults to logging.WARNING to suppress successes.
        Set level of logging to logging.DEBUG to see all tests.
        """
        self._log_level = log_level
        if self._log_level == "DEBUG":
            logging.basicConfig(level=logging.DEBUG)
        elif self._log_level == "ERROR":
            logging.basicConfig(level=logging.ERROR)
        else:
            logging.basicConfig(level=logging.WARNING)

        # Initialize Instance Attributes that are used later
        self._test_name = 'None'

    def print_test_begin(self, test_name):
        """
        @param test_name: Name of test being run

        Prints a line before test assertions so one knows the test is running.
        """
        self._test_name = test_name
        log = logging.getLogger(self._test_name)
        log.debug("...")

    def print_test_success(self, test_name):
        """
        @param test_name: Name of test being run

        Prints a line for success if the test succeeds.
        """
        self._test_name = test_name
        log = logging.getLogger(self._test_name)
        log.debug("Success\n")

    def print_test_failure(self, test_name):
        """
        @param test_name: Name of test being run

        Prints a line for failure if the test fails.
        """
        self._test_name = test_name
        log = logging.getLogger(self._test_name)
        if self._log_level == "ERROR":
            log.exception("FAILURE\n")
        else:
            log.warning("FAILURE\n")

    def print_test_failure_exception(self, test_name):
        """
        @param test_name: Name of test being run

        Prints an exception block for failure if the test fails.
        """
        self._test_name = test_name
        log = logging.getLogger(self._test_name)
        log.exception("FAILURE\n")
