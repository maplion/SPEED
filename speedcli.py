#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command-Line Interface Module for handling command-line arguments.

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import os
import argparse

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"


class SpeedCLI(object):

    def __init__(self, description="SPEED Program"):
        """
        SpeedCLI Constructor
        """

        # Initialize Variables
        self._argv = None
        self._args = None
        self._path = None
        self._inputFilePath = None
        self._description = description
        self._parser = None
        self._defaultInputDataFilePath = "/data"
        self._defaultOutputDataFilePath = "/output"

        # Setup argParse
        self._parser = argparse.ArgumentParser(description=self._description)

        self._parser.add_argument("-i", action="store", dest="file",
                                  help="The name of the file from which to load data.")
        self._parser.add_argument("-i2", action="store", dest="file2",
                                  help="The name of the second file from which to load data.")
        self._parser.add_argument("-d", action="store", dest="date",
                                  help="If desired, choose a specific date to read from the file (e.g. 01/01/2014)")
        self._parser.add_argument("-ipath", action="store", dest="inputFilePath",
                                  default=self._defaultInputDataFilePath, help="The path to the file")
        self._parser.add_argument("-o", action="store", dest="outputFile",
                                  help="If desired, supply the name of a file to print console output to.")
        self._parser.add_argument("-opath", action="store", dest="outputFilePath",
                                  default=self._defaultOutputDataFilePath,
                                  help="The path if you want the output file to go "
                                       "somewhere other than the default output folder.")

    def argParse(self, args):
        """
        Parses incoming arguments and returns an argparse object to use in the rest of the program.

        @param args: Incoming Arguments
        @returns: argparse parsed argument object
        """
        self._args = args
        _results = self._parser.parse_args(args[1:])
        if _results.inputFilePath == self._defaultInputDataFilePath:
            _head, _tail = os.path.split(args[0])
            _results.inputFilePath = _head + self._defaultInputDataFilePath
            self.createDirectory(_results.inputFilePath)
        if _results.outputFilePath == self._defaultOutputDataFilePath:
            _head, _tail = os.path.split(args[0])
            _results.outputFilePath = _head + self._defaultOutputDataFilePath
            self.createDirectory(_results.outputFilePath)
        return _results

    def createDirectory(self, path):
        """
        Checks if a directory exists; if it does not, creates it.

        @param path: Path of directory to be created
        """
        self._path = path
        if not os.path.exists(self._path):
            os.makedirs(self._path)
