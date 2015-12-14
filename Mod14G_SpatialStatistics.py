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

        # Read GAL file for a rooks weight matrix
        Morans_I = sc_ss.calc_Morans_I(rasterArray)

        # Process Spatial Statistics

        # Save array out to Spatial Raster (GeoTiff)
        if arguments.outputFile is None:
            if ".tif" in arguments.file:
                arguments.file.replace(".tif", "")
            arguments.outputFile = arguments.file + "_MoransI"
        outputFilename = arguments.outputFilePath + "/" + arguments.outputFile + ".tif"
        # sc_ss.saveRasterArrayToGeoTiff(rasterArray, outputFilename)

        outputImage = None
        if ".tif" in arguments.file:
                outputImage = arguments.outputFilePath + "/" + arguments.file.replace(".tif", "")

        end_time = time.clock()
        execution_time = end_time - start_time
        print "Process time: {0}".format(execution_time)

        lag_distance = sc_ss.getLagDistanceForPlot(30, 330)

        # Save out image of related NDVI
        figure(1)
        title('NDVI Image {0}'.format(arguments.file))
        imshow(rasterArray)
        savefig(outputImage + "_NDVI.jpg", dpi=300)
        # show()

        # Save out image of Plot of Lag Distance vs. Moran's I number
        figure(2)
        plot(lag_distance, Morans_I, 'bo')
        title('Spatial Autocorrelation of NDVI for Image {0}'.format(arguments.file))
        xlabel('Lag Distance(m)')
        ylabel('Morans I')
        savefig(outputImage + "_plot.jpg", dpi=300)
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
