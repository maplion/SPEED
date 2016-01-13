#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 14: Spatial Statistics

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import threading

from matplotlib.pylab import *

import speedcalc
import speedcli
from testcalculations import time

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_ss = speedcalc.SpatialStatistics()
s_cli = speedcli.SpeedCLI(description="SPEED Spatial Statistics")

# Progress bar variables
stop = False
kill = False


class ProgressBarLoading(threading.Thread):
    """
    Self-made animated spinner for the purpose of letting the user know that something
    is processing; built for an unknown process time with know gauges.
    """

    def run(self):
            global stop
            global kill
            i = 0
            while not stop:
                if (i % 4) == 0:
                    sys.stdout.write('Loading... /')
                    time.sleep(0.2)
                    sys.stdout.write('\r')
                elif (i % 4) == 1:
                    sys.stdout.write('Loading... -')
                    time.sleep(0.2)
                    sys.stdout.write('\r')
                elif (i % 4) == 2:
                    sys.stdout.write('Loading... \\')
                    time.sleep(0.2)
                    sys.stdout.write('\r')
                elif (i % 4) == 3:
                    sys.stdout.write('Loading... |')
                    time.sleep(0.2)
                    sys.stdout.write('\r')

                sys.stdout.flush()
                time.sleep(0.1)
                i += 1

            if kill:
                print 'ABORT!\n\n',
            else:
                print 'Done!\n\n',


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    """
    This is the main function for Module 14

    @param argv: incoming arguments
    @return: void
    """

    # Start time and Progress Bar
    start_time = time.clock()
    p = ProgressBarLoading()
    p.start()
    global stop
    global kill

    # Declare local main Variables
    if argv is None:
        argv = sys.argv

    try:
        # Parse command line arguments
        arguments = s_cli.arg_parse(argv)

        # Get File
        if arguments.file is None:
            sys.exit("No file name given.")
        else:
            filename = arguments.inputFilePath + "/" + arguments.file
            if ".tif" not in filename:
                filename += ".tif"

        # Read Raster into an Array
        rasterArray = sc_ss.read_raster_as_array(filename)

       # Process Spatial Statistics
        Morans_I = sc_ss.calc_morans_i(rasterArray)

        # Save array out to Spatial Raster (GeoTiff)
        if arguments.outputFile is None:
            if ".tif" in arguments.file:
                arguments.file.replace(".tif", "")
            arguments.outputFile = arguments.file + "_MoransI"
        # outputFilename = arguments.outputFilePath + "/" + arguments.outputFile + ".tif"
        # sc_ss.save_raster_array_to_geotiff(rasterArray, outputFilename)

        outputImage = None
        if ".tif" in arguments.file:
                outputImage = arguments.outputFilePath + "/" + arguments.file.replace(".tif", "")

        end_time = time.clock()
        execution_time = end_time - start_time
        time.sleep(1)
        stop = True
        print "\n\nProcess time: {0} seconds".format(round(execution_time, 2))

        lag_distance = sc_ss.get_lag_distance_for_plot(30, 330)

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

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

    except KeyboardInterrupt or EOFError:
        kill = True
        stop = True

if __name__ == "__main__":
    sys.exit(main())
