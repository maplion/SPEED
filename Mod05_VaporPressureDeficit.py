#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 05: Calculating Vapor Pressure Deficit.

Computes values of VPD for a 24 hour period at a meteorological station in the Dry Creek Experimental Watershed

Note: methods (and their specific names) included in this module are here to meet the listed requirements

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import sys
import getopt
import time
import speedcalc
import speedloader

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_Pressure = speedcalc.Pressure()
sl = speedloader.SpeedLoader()
sl_dc = speedloader.DryCreek()


def getSatVaporPressure(temperature):
    """
    Gets the Saturation Vapor Pressure

    @param temperature: Temperature in Celsius
    @return: Saturation Vapor Pressure
    """
    _temperature = temperature
    _result = sc_Pressure.vaporPressure_fromTemperature(_temperature)
    return _result


def getVaporPressure(temperature, relativeHumidity):
    """
    Gets the vapor Pressure

    @param temperature: Temperature in Celsius
    @return: Vapor Pressure
    """
    _temperature = temperature
    _relativeHumidity = relativeHumidity
    _satVaporPressure = getSatVaporPressure(_temperature)
    _vaporPressure = sc_Pressure.vaporPressure_fromRelativeHumidity(_relativeHumidity, _satVaporPressure)
    return _satVaporPressure, _vaporPressure


def getVPD(temperature, relativeHumidity):
    """
    Gets the Vapor Pressure Deficit (VPD)

    @param temperature: Temperature in Celsius
    @return: Saturation Vapor Pressure
    """
    _temperature = temperature
    _relativeHumidity = relativeHumidity
    _satVaporPressure, _vaporPressure = getVaporPressure(_temperature, _relativeHumidity)
    _result = sc_Pressure.vaporPressureDeficit(_satVaporPressure, _vaporPressure)
    return _result


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    """

    Reference: https://www.artima.com/weblogs/viewpost.jsp?thread=4829
    """
    if argv is None:
        argv = sys.argv
    try:
        # try:
        #     opts, args = getopt.getopt(argv[1:], "h", ["help"])
        # except getopt.error, msg:
        #     raise Usage(msg)

        #filename = sl.openFileDialog_gui()
        filename = u"C:/Users/MapLion/Documents/BSU_BoiseStateUniversity/GEOS597/Module 5/LDP_HrlySummary_2014.csv"
        data, headers = sl_dc.weatherStationData_csv(filename)
        dateIndex, dateTitle = sl_dc.getColumnIndexAndName("Date", headers)
        relativeHumidityIndex, relativeHumidityTitle = sl_dc.getColumnIndexAndName("Humidity", headers)
        temperatureIndex, temperatureTitle = sl_dc.getColumnIndexAndName("Temp", headers)

        dateData = sl_dc.getColumn(dateIndex, data)
        dates = sl_dc.convertDate(dateData)
        relativeHumidityData = sl_dc.getColumn(relativeHumidityIndex, data)
        temperatureData = sl_dc.getColumn(temperatureIndex, data)

        day = 11
        month = 1
        year = 2014

        #Start count at 21 for numbering to match Excel files, calculate VPD and print result
        i = 21
        for date, relativeHumidity, temp in zip(dates, relativeHumidityData, temperatureData):
            # print str(i) + ". " + str(date) + " " + str(relativeHumidity) + " " + temp
            if date[0] == year and date[1] == month and date[2] == day:
                satVaporPressure = sc_Pressure.vaporPressure_fromTemperature(float(temp))
                vaporPressure = sc_Pressure.vaporPressure_fromRelativeHumidity(float(relativeHumidity), float(satVaporPressure))
                print (satVaporPressure - vaporPressure)/1000
                vpd = getVPD(float(temp), float(relativeHumidity))
                vpd = sc_Pressure.pascalsTo_kiloPascals(vpd)
                print str(i) + ". " + time.strftime('%m/%d/%Y', date) + " " + str(relativeHumidity) + " " + temp +\
                    " => VPD: " + str(vpd)
            i += 1

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())

