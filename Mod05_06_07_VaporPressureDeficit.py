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
import Tkinter as tk
import speedcalc
import speedloader
import speedgui

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_Pressure = speedcalc.Pressure()
sg = speedgui.SpeedGUI()
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
    This is the main function for Module 05, 06, 07

    main() function style Reference: https://www.artima.com/weblogs/viewpost.jsp?thread=4829
    """
    # TODO: Create Command Line Switch (gui/console)
    # TODO: Create Command Line Tools (parse command line)
    # TODO: Create Command Line Validation
    # TODO: Create Output to file from Command Line
    # TODO: Create Standalone executable.

    # Declare local main Variables
    gui = "false"
    filename = None
    root = None  # root window for tkinter
    text = None  # Text
    day = None
    month = None
    year = None

    if argv is None:
        argv = sys.argv
        gui = "true"
    else:
        pass
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)

        # Get File
        if gui:
            filename = sg.openFileDialog()
        else:
            pass

        # filename = u"C:/Users/MapLion/Documents/BSU_BoiseStateUniversity/GEOS597/Module 5/LDP_HrlySummary_2014.csv"

        # Check if fileDialog was cancelled and exit if it was
        if filename == '':
            sys.exit()

        if gui:
            # Date entry form for GUI (reference: http://www.python-course.eu/tkinter_entry_widgets.php)
            fields = 'Month', 'Day', 'Year'
            root = sg._root
            root.update()
            root.deiconify()
            ents = sg.makeForm(root, fields)
            root.bind('<Return>', (lambda event, e=ents: sg.fetch(e)))
            b1 = tk.Button(root, text='Go', command=(lambda e=ents: sg.fetch(e, lastCall="true")))
            b1.pack(side=tk.LEFT, padx=5, pady=5)
            b2 = tk.Button(root, text='Quit', command=root.quit)
            b2.pack(side=tk.LEFT, padx=5, pady=5)
            root.mainloop()

            # Set Date
            entries = sg.getEntries()
            day = entries['Day']
            month = entries['Month']
            year = entries['Year']
            day = int(day)
            month = int(month)
            year = int(year)

        else:
            pass

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

        if gui:
            # Create Textbox output box for GUI
            root = tk.Tk()
            scrollbar = tk.Scrollbar(root)
            text = tk.Text(root, height=50, width=100)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            text.pack(side=tk.LEFT, fill=tk.Y)
            scrollbar.config(command=text.yview)
            text.config(yscrollcommand=scrollbar.set)
        else:
            pass

        # Calculate VPD and print result; start count at 21 for numbering to match csv line numbers when read in Excel
        # for visual reference

        # Print Headers
        if gui:
            text.insert(tk.END, "\t Date\t     " + relativeHumidityTitle + "\t\t" + temperatureTitle +
                        "\t\t\tVapor Pressure Deficit (kPa)\n")
            text.insert(tk.END, "------------------------------------------------------------------------------------" +
                                "------\n")
        else:
            print("\t Date\t     " + relativeHumidityTitle + "\t\t" + temperatureTitle +
                  "\t\t\tVapor Pressure Deficit (kPa)\n")
            print("------------------------------------------------------------------------------------" +
                  "----------------------------\n")
        recordCount = 0  # found record count
        i = 21  # line count
        for date, relativeHumidity, temp in zip(dates, relativeHumidityData, temperatureData):
            if date[0] == year and date[1] == month and date[2] == day:
                vpd = getVPD(float(temp), float(relativeHumidity))
                vpd = sc_Pressure.pascalsTo_kiloPascals(vpd)
                outputLine = str(i) + ". " + time.strftime('%m/%d/%Y', date) + "\t\t\t RH: " + str(relativeHumidity) +\
                    "\t\t     T: " + temp + "\t\t\t=> VPD: " + str(vpd) + "\n"

                if gui:
                    text.insert(tk.END, outputLine)
                else:
                    print outputLine

                recordCount += 1
            i += 1
        if recordCount == 0:
            if gui:
                text.insert(tk.END, "No records found for the date given.")
            else:
                print "No records found for the date given."
        if gui:
            text.config(state=tk.DISABLED)  # Make output textbox readonly
            root.mainloop()  # Note: destroying root and creating a new one with second mainloop isn't ideal.
        else:
            pass

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())

