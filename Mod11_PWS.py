#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 11: Calculating Plant Water Stress

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import sys
import time
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
        else:
            filename = arguments.inputFilePath + "/" + arguments.file
            if ".csv" not in filename:
                filename += ".csv"

        # parse file
        data, headers = sl_dc.standard_csv(filename)
        dateIndex, dateTitle = sl_dc.getColumnIndexAndName("Date", headers)
        soilMoistureIndex, soilMoistureTitle = sl_dc.getColumnIndexAndName("Soil_Moisture", headers)

        # parse column data
        # dateData = sl_dc.getColumn(dateIndex, data)
        # dates = sl_dc.convertDate_mdY_HMS(dateData)
        soilMoistureData = sl_dc.getColumn(soilMoistureIndex, data)

        # Calculate Plant Water Stress
        changeInTime = 1.0  # in hours [time at k+1 minus time at k]
        waterMoisture = 0.17  # theta_star
        PWS = sc_PWS.calculate_PWS(soilMoistureData, changeInTime, waterMoisture)

        end_time = time.clock()
        execution_time = end_time - start_time
        print "Plant Water Stress: {0}".format(PWS)

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
