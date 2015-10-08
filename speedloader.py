#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for loading data from files

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import time

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
    Dry Creek Experimental Watershed (DCEW): http://earth.boisestate.edu/drycreek/
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
        self._string = None
        self._tableHeaders = None

    def weatherStationData_csv(self, filename):
        """
        Extracts Dry Creek Experimental Watershed weather station data (in the format downloaded from the site)

        @param filename: the full path plus the file name
        @return: returns a list of the data and their headers
        """
        self._filename = filename

        with open(self._filename) as _csvfile:
            # Skip Headers
            _lines_after_header = _csvfile.readlines()[19:]
            _csvfile.close()  # Usually not necesary with "with", but ensuring closure

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
            parsedRow = row.split(',')
            _column.append(parsedRow[self._index])
        return _column

    def convertDate(self, dates):
        self._dates = dates
        _date = []
        for date in dates:
            _date.append(time.strptime(date, '%m/%d/%Y %H:%M'))
        return _date
