#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for creating GUI elements

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import Tkinter as tk
from tkFileDialog import askopenfilename

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"


class SpeedGUI(object):

    def __init__(self):
        """
        SpeedGUI Constructor
        """

        # Initialize Variables
        self._root = None
        self._fields = None
        self._entries = None

    def getRoot(self):
        """
        Gets the root window
        @returns root
        """
        return self._root

    def openFileDialog(self):
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

    def getEntries(self):
        """
        Returns the gui form _entries

        @return: gui form _entries
        """
        return self._entries

    def makeForm(self, root, fields):
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

    def fetch(self, entries, lastCall="false"):
        """
        Fetches the data from the gui frame; closes out window if it is the last call

        @param entries: the user's _entries into the form
        @param lastCall: if set to true, will close out the window
        @return: void
        """
        self._entries = entries
        _result = {}
        for entry in self._entries:
            _result[entry[0]] = entry[1].get()
        if lastCall == "true":
            self._root.destroy()
        self._entries = _result
