#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 09: Polygon Class

Utilizes a self-made Polygon Class and calculates the Area, Centroid, and Perimeter from given polygon coordinates.

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import sys
import numpy as np
import speedcalc
import speedcli

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

s_cli = speedcli.SpeedCLI(description="SPEED Polygon Class")
sc = speedcalc

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    """
    This is the main function for Module 09
    """

    try:
        # Declare local main Variables
        if argv is None:
            argv = sys.argv

        arguments = s_cli.arg_parse(argv)

        if arguments.file is None:
            sys.exit("No file was given as an input.")
        else:
            filename = arguments.inputFilePath + "/" + arguments.file

        # Read csv file - x and y of Polygon
        x_poly, y_poly = np.genfromtxt(filename, dtype=float, unpack=True, delimiter=',', skip_header=1)
        try:
            TodaysPoly = sc.Polygon(x_poly, y_poly)  # Instantiate TodaysPoly with given x,y coordinates
        except ValueError as e:
            sys.exit(e)  # Exit if given coordinates were an invalid polygon

        # Print results
        print("Polygon Area: " + str(TodaysPoly.get_poly_area()))
        print("Polygon Centroid: " + str(TodaysPoly.get_poly_centroid()))
        print("Polygon Perimeter: " + str(TodaysPoly.get_poly_perimeter()))

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
