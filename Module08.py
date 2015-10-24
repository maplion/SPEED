#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 08: numpy, arrays, and plots

Takes input from a csv file, creates an array and determines the first,
second and third order polynomial function of the data.

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

from matplotlib.pylab import *
import speedcli

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

s_cli = speedcli.SpeedCLI(description="SPEED First, Second, and Third Order Polynomial from Array Data")


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    """
    This is the main function for Module 08
    """

    outputFilePath = None

    try:
        # Declare local main Variables
        if argv is None:
            argv = sys.argv

        arguments = s_cli.argParse(argv)

        if arguments.file is None:
            sys.exit("No file was given as an input.")
        else:
            filename = arguments.inputFilePath + "/" + arguments.file

        if arguments.outputFile is None:
            arguments.outputFile = "RDD_Module08.jpg"

        if arguments.outputFile is not None:
            outputFilePath = arguments.outputFilePath + "/" + arguments.outputFile

        # Read csv file - x is Elevation and y is annual precipitation in millimeters
        x_elevation, y_annual_precip = np.genfromtxt(filename, dtype=float, unpack=True, delimiter=',', skip_header=1)

        first_order_poly = np.polyfit(x_elevation, y_annual_precip, 1)
        first_order_poly = np.poly1d(first_order_poly)

        second_order_poly = np.polyfit(x_elevation, y_annual_precip, 2)
        second_order_poly = np.poly1d(second_order_poly)

        third_order_poly = np.polyfit(x_elevation, y_annual_precip, 3)
        third_order_poly = np.poly1d(third_order_poly)

        l = np.linspace(min(x_elevation), max(x_elevation), 50)

        # Plots
        plot(x_elevation, y_annual_precip, 'bo', label='input data')
        hold('on')
        plot(l, first_order_poly(l), 'r-', l, second_order_poly(l), 'g-', l, third_order_poly(l), 'b-')
        xlabel('Elevation (m)')
        ylabel('Annual Precipitation (mm)')
        legend(['SNOTEL Data', 'First order', 'Second order', 'Third order'], loc='upper left')
        savefig(outputFilePath, dpi=300)
        show()

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
