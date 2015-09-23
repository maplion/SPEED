#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for loading data from files

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

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
        pass

    def gui_openFileDialog(self):
        """
        Opens a basic file dialog that browses to a file

        @returns: path and filename
        Reference: http://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog
        """
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        return filename

    def cmd_argumentParse(self):
        """
        """
        pass


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
        self._filename = 'None'

    def weatherStationData(self, filename):
        """
        @param filename:
        @return:
        """
        self._filename = filename
        print self._filename