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
# import getopt
import time
import Tkinter as tk
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

        # Get File
        filename = sl.openFileDialog_gui()
        # filename = u"C:/Users/MapLion/Documents/BSU_BoiseStateUniversity/GEOS597/Module 5/LDP_HrlySummary_2014.csv"

        # Check if fileDialog was cancelled
        if filename == '':
            sys.exit()

        # Date entry form (reference: http://www.python-course.eu/tkinter_entry_widgets.php)
        fields = 'Month', 'Day', 'Year'
        root = sl._root
        root.update()
        root.deiconify()
        ents = sl.makeForm(root, fields)
        root.bind('<Return>', (lambda event, e=ents: sl.fetch(e)))
        b1 = tk.Button(root, text='Go', command=(lambda e=ents: sl.fetch(e, lastCall="true")))
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        b2 = tk.Button(root, text='Quit', command=root.quit)
        b2.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

        # Set Date
        # day = 11
        # month = 7
        # year = 2014
        entries = sl.entries
        day = entries['Day']
        month = entries['Month']
        year = entries['Year']
        day = int(day)
        month = int(month)
        year = int(year)

        # TODO: Add Validation: Validate Date

        # parse file
        data, headers = sl_dc.weatherStationData_csv(filename)
        dateIndex, dateTitle = sl_dc.getColumnIndexAndName("Date", headers)
        relativeHumidityIndex, relativeHumidityTitle = sl_dc.getColumnIndexAndName("Humidity", headers)
        temperatureIndex, temperatureTitle = sl_dc.getColumnIndexAndName("Temp", headers)

        # parse column data
        dateData = sl_dc.getColumn(dateIndex, data)
        dates = sl_dc.convertDate(dateData)
        relativeHumidityData = sl_dc.getColumn(relativeHumidityIndex, data)
        temperatureData = sl_dc.getColumn(temperatureIndex, data)

        root = tk.Tk()
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=50, width=100)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        # Calculate VPD
        # Start count at 21 for numbering to match Excel files, calculate VPD and print result
        i = 21
        for date, relativeHumidity, temp in zip(dates, relativeHumidityData, temperatureData):
            if date[0] == year and date[1] == month and date[2] == day:
                vpd = getVPD(float(temp), float(relativeHumidity))
                vpd = sc_Pressure.pascalsTo_kiloPascals(vpd)
                outputLine = str(i) + ". " + time.strftime('%m/%d/%Y', date) + "\t\t\tRH: " + str(relativeHumidity) +\
                    "\t\tT: " + temp + "\t\t=> VPD: " + str(vpd) + "\n"
                T.insert(tk.END, outputLine)
            i += 1
        root.mainloop()  # Note: destroying root and creating a new one with second mainloop isn't ideal, but it works.

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())

