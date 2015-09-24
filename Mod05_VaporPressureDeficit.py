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
    _result = sc_Pressure.vaporPressure_fromRelativeHumidity(_relativeHumidity, _satVaporPressure)
    return _result


def getVPD(temperature, relativeHumidity):
    """
    Gets the Vapor Pressure Deficit (VPD)

    @param temperature: Temperature in Celsius
    @return: Saturation Vapor Pressure
    """
    _temperature = temperature
    _relativeHumidity = relativeHumidity
    _satVaporPressure = getSatVaporPressure(_temperature)
    _vaporPressure = getVaporPressure(_temperature, _relativeHumidity)
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
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)

        #filename = sl.openFileDialog_gui()
        filename = u"C:/Users/MapLion/Documents/BSU_BoiseStateUniversity/GEOS597/Module 5/LDP_HrlySummary_2014.csv"
        data, headers = sl_dc.weatherStationData_csv(filename)
        dateIndex, dateTitle = sl_dc.getColumnIndexAndName("Date", headers)
        precipIndex, precipTitle = sl_dc.getColumnIndexAndName("Precipitation", headers)
        temperatureIndex, temperatureTitle = sl_dc.getColumnIndexAndName("Temp", headers)

        dateData = sl_dc.getColumn(dateIndex, data)
        dates = sl_dc.convertDate(dateData)
        precipData = sl_dc.getColumn(precipIndex, data)
        temperatureData = sl_dc.getColumn(temperatureIndex, data)

        # for i in range(1, len(precipData)):
        #     print temperatureData[i]
        #     print precipData[i]
        #     vpd = getVPD(temperatureData[i], precipData[i])
        #     vpd = sc_Pressure.pascalsTo_kiloPascals(vpd)
        #     print(vpd)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())

