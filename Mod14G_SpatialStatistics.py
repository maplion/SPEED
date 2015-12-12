#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 14: Spatial Statistics

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import time
from matplotlib.pylab import *
# import timeit
import speedcalc
import speedcli

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_ss = speedcalc.SpatialStatistics()
s_cli = speedcli.SpeedCLI(description="SPEED Spatial Statistics")
# total_time = timeit.timeit('[v for v in range(10000)]', number=10000)


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    """
    This is the main function for Module 14

    @param argv: incoming arguments
    @return: void
    """

    start_time = time.clock()
    # Declare local main Variables
    if argv is None:
        argv = sys.argv

    try:
        # Parse command line arguments
        arguments = s_cli.argParse(argv)

        # Get File
        if arguments.file is None:
            sys.exit("No file name given.")
        else:
            filename = arguments.inputFilePath + "/" + arguments.file
            if ".tif" not in filename:
                filename += ".tif"

        # Read Raster into an Array
        rasterArray = sc_ss.readRasterAsArray(filename)

        # Process Spatial Statistics

        # Save array out to Spatial Raster (GeoTiff)
        if arguments.outputFile is None:
            if ".tif" in arguments.file:
                arguments.file.replace(".tif", "")
            arguments.outputFile = arguments.file + "_MoransI.tif"
        outputFilename = arguments.outputFilePath + "/" + arguments.outputFile
        sc_ss.saveRasterArrayToGeoTiff(rasterArray, outputFilename)

        end_time = time.clock()
        execution_time = end_time - start_time

        show()

        # Benchmarking
        # print "Single Execution Time: {0} seconds".format(round(execution_time, 6))
        # print "Total wall-clock time to execute the statement 10000 times: {0}".format(total_time)
        # print "Average time per loop: {0}".format(total_time/10000)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
