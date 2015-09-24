#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for loading data from files

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import time
from Tkinter import Tk
from tkFileDialog import askopenfilename

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"


class SpeedLoader(object):

    def __init__(self):
        """
        SpeedLoader Constructor
        """

        # Initialize Variables
        self._myList = None
        self._myString = None

    def openFileDialog_gui(self):
        """
        Opens a basic file dialog that browses to a file

        @returns: path and filename
        Reference: http://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog
        """
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        _filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        return _filename

    def argumentParse_cmd(self):
        """
        Stubbed method
        """
        pass

    def substring(self, myString, myList):
        """
        Find substring finds a particular string within a list

        @param myString: The string that is being searched for in the list
        @param myList: The list where one wants to find the string
        """
        self._myList = myList
        self._myString = myString.lower()
        return [i for i, val in enumerate(self._myList) if self._myString in val.lower()]

class DryCreek(SpeedLoader):  # subclass, inherits from SpeedLoader
    """
    Subclass for SpeedLoader created for the purpose
    of organization within the SpeedLoader superclass;
    These are loads specifically for data coming from the
    Dry Creek Experimental Watershed (DCEW)
    """

    def __init__(self):
        """
        Initializes subclass DryCreek
        """
        super(SpeedLoader, self).__init__()

        # Initialize Variables
        self._filename = None
        self._index = None
        self._dataRows = None
        self._dates = None

    def weatherStationData_csv(self, filename):
        """
        @param filename:
        @return:
        """
        self._filename = filename

        with open(self._filename) as _csvfile:
            # Skip Headers
            _lines_after_header = _csvfile.readlines()[19:]
            _csvfile.close()

        # for row in _lines_after_header:
        #     print row

        _tableHeaders = _lines_after_header[0].split(',')
        #
        # for header in _tableHeaders:
        #     print header

        return _lines_after_header[1:], _tableHeaders

    def getColumnIndexAndName(self, string, tableHeaders):
        """
        Returns the index and name of the first header that is found with a name like the string given.
        With this information, one can grab the column from the csv that they desire.

        @param string: The header name that is being searched within the column titles
        @param tableHeaders: The list of column titles (from the parsed csv)
        @return: the index and name of the first header that is found with the given string name
        """
        self._string = string
        self._tableHeaders = tableHeaders
        _headerIndex = self.substring(self._string, self._tableHeaders)
        _headerName = self._tableHeaders[_headerIndex[0]]
        return _headerIndex[0], _headerName

    def getColumn(self, index, dataRows):
        """
        Takes the csv data table and parses out a particular _column based on the index of that _column
        (found using getColumnIndexAndName)

        @param index: index of the _column
        @param dataRows: the list of rows of the data that includes all columns
        @returns: the _column of data values as a parsed list (removing other _column data)
        """
        self._index = index
        self._dataRows = dataRows
        _column = []
        for row in dataRows:
            for value in row.split(','):
                # if value == -6999:
                #     value = None
                _column.append(value)
                print _column[self._index]
        return _column[self._index]

    def convertDate(self, dates):
        self._dates = dates
        _structDate = []
        for date in dates:
            _structDate.append(time.strptime(date, '%d/%m/%Y %H'))
            print _structDate
        return _structDate