#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for loading data from files

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import time
import Tkinter as tk
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
        self._root = None
        self._fields = None
        self._entries = None

    def openFileDialog_gui(self):
        """
        Opens a basic file dialog that browses to a file

        @returns: path and filename
        Reference: http://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog
        Reference: http://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/
        """
        self._root = tk.Tk()
        self._root.withdraw()  # we don't want a full GUI, so keep the root window from appearing
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

    def getEntries_gui(self):
        """
        Returns the gui form _entries
        @return gui form _entries
        """
        return self._entries

    def makeForm_gui(self, root, fields):
        """
        Creates a gui frame

        @param root: the root gui object
        @param fields: the fields to build in the gui
        @return: void
        """
        self._root = root
        self._fields = fields
        _entries = []
        for field in self._fields:
            row = tk.Frame(self._root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            _entries.append((field, ent))
        return _entries

    def fetch_gui(self, entries, lastCall="false"):
        """
        Fetches the data from the gui frame; closes out window if it is the last call

        @param entries: the user's _entries into the form
        @param lastCall: if set to true, will close out the window
        @return: void
        """
        self._entries = entries
        _result = {}
        for entry in self._entries:
            field = entry[0]
            text = entry[1].get()
            # print('%s: "%s"' % (field, text))
            _result[entry[0]] = entry[1].get()
        if lastCall == "true":
            self._root.destroy()
        self._entries = _result


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
            parsedRow = row.split(',')
            _column.append(parsedRow[self._index])
        return _column

    def convertDate(self, dates):
        self._dates = dates
        _date = []
        for date in dates:
            _date.append(time.strptime(date, '%m/%d/%Y %H:%M'))
        return _date