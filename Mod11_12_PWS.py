#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 11: Calculating Plant Water Stress

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import time
from matplotlib.pylab import *
# import timeit
import speedcalc
import speedloader
import speedcli

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sl_dc = speedloader.CSV()
s_cli = speedcli.SpeedCLI(description="SPEED Plant Water Stress Command Line Interface")
sc_PWS = speedcalc.PlantWaterStress()
# total_time = timeit.timeit('[v for v in range(10000)]', number=10000)


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    """
    This is the main function for Module 11

    @param argv: incoming arguments
    @return: void
    """

    start_time = time.clock()
    # Declare local main Variables
    if argv is None:
        argv = sys.argv

    try:
        arguments = s_cli.argParse(argv)

        # get File
        if arguments.file is None:
            sys.exit("No file name given.")
        if arguments.file2 is None:
            sys.exit("No file name given for second file")
        else:
            filename = arguments.inputFilePath + "/" + arguments.file
            if ".csv" not in filename:
                filename += ".csv"
            filename2 = arguments.inputFilePath + "/" + arguments.file2
            if ".csv" not in filename2:
                filename2 += ".csv"

        # parse file
        data, headers = sl_dc.standard_csv(filename)
        data2, headers2 = sl_dc.standard_csv(filename2)
        dateIndex, dateTitle = sl_dc.getColumnIndexAndName("Date", headers)
        dateIndex2, dateTitle2 = sl_dc.getColumnIndexAndName("Date", headers2)
        soilMoistureIndex, soilMoistureTitle = sl_dc.getColumnIndexAndName("Soil_Moisture", headers)
        soilMoistureIndex2, soilMoistureTitle2 = sl_dc.getColumnIndexAndName("Soil_Moisture", headers2)

        dayPieces = data[0].split('/')
        dayPieces2 = data2[0].split('/')
        year = int(dayPieces[2][:4])
        year2 = int(dayPieces2[2][:4])

        # parse column data
        # dateData = sl_dc.getColumn(dateIndex, data)
        # dates = sl_dc.convertDate_mdY_HMS(dateData)
        soilMoistureData = sl_dc.getColumn(soilMoistureIndex, data)
        soilMoistureData2 = sl_dc.getColumn(soilMoistureIndex2, data2)

        # Calculate Plant Water Stress
        timeInterval = 1.0  # in hours [time at k+1 minus time at k]
        waterMoisture = 0.17  # theta_star
        PWS = sc_PWS.calculate_PWS(soilMoistureData, timeInterval, waterMoisture)
        PWS_file2 = sc_PWS.calculate_PWS(soilMoistureData2, timeInterval, waterMoisture)

        PWS2_file1 = sc_PWS.calculate_PWS2(soilMoistureData, timeInterval)
        PWS2_file2 = sc_PWS.calculate_PWS2(soilMoistureData2, timeInterval)

        end_time = time.clock()
        execution_time = end_time - start_time
        print "Plant Water Stress: {0}".format(PWS)
        print "Plant Water Stress: {0}".format(PWS_file2)
        # print "PWS2 {1}: {0}".format(PWS2_file1, year)
        # print "PWS2 {1}: {0}".format(PWS2_file2, year2)

        # Plot results for PWS2
        x_data2 = linspace(1, PWS2_file1.size, PWS2_file1.size)
        plot(x_data2, PWS2_file1, 'ro', x_data2, PWS2_file2, 'b*')
        title('PWS2 at {0} and {1}'.format(year, year2))
        xlabel('Time(hr)')
        ylabel('PWS2')
        legend(['PWS2 2007', 'PWS2 2011'])

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
