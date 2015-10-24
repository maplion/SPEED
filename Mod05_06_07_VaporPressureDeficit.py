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
import time
import Tkinter as tk
import speedcalc
import speedloader
import speedgui
import speedcli

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_Pressure = speedcalc.Pressure(numberOfDecimals=2)
sg = speedgui.SpeedGUI()
sl_dc = speedloader.DryCreek()
s_cli = speedcli.SpeedCLI(description="SPEED Vapor Pressure Deficit Command Line Interface")


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

    # TODO: Check for output directory and create them if they don't exist
    # TODO: Create Command Line Validation; Add Date Validation
    # TODO: Create Output to file from Command Line
    # TODO: Create Standalone executable.

    # Declare local main Variables
    if argv is None:
        argv = sys.argv
    gui = False
    root = None  # root window for tkinter
    text = None  # Text
    day = None
    month = None
    year = None
    showAll = False
    arguments = None

    try:
        if len(argv) == 1:
            gui = True
        else:
            arguments = s_cli.argParse(argv)

        # Get File
        if gui:
            filename = sg.openFileDialog()
        else:
            filename = arguments.inputFilePath + "/" + arguments.file

        # filename = u"C:/Users/MapLion/Documents/BSU_BoiseStateUniversity/GEOS597/Module 5/LDP_HrlySummary_2014.csv"

        # Check if fileDialog was cancelled and exit if it was
        if filename == '':
            sys.exit()

        if gui:
            # Date entry form for GUI (reference: http://www.python-course.eu/tkinter_entry_widgets.php)
            fields = 'Month', 'Day', 'Year'
            root = sg.getRoot()
            root.update()
            root.deiconify()
            ents = sg.makeForm(root, fields)
            root.bind('<Return>', (lambda event, e=ents: sg.fetch(e)))
            checkVar = tk.IntVar()
            checkbox = tk.Checkbutton(root, text="Show All:", variable=checkVar)
            checkbox.pack(side=tk.LEFT, padx=5, pady=5)
            b1 = tk.Button(root, text='Go', command=(lambda e=ents: sg.fetch(e, lastCall=True)))
            b1.pack(side=tk.LEFT, padx=5, pady=5)
            b2 = tk.Button(root, text='Quit', command=root.quit)
            b2.pack(side=tk.LEFT, padx=5, pady=5)
            root.mainloop()

            # An imperfect way to ensure a clean exit when "Quit" is clicked in the GUI.
            if sg.getEntries() is None:
                sys.exit()
            # Set Date
            entries = sg.getEntries()
            day = entries['Day']
            month = entries['Month']
            year = entries['Year']
            day = int(0 if day == '' or day is None else day)
            month = int(0 if month == '' or month is None else month)
            year = int(0 if year == '' or year is None else year)
            showAll = checkVar.get()

        else:
            if arguments.date is None:
                showAll = True
            else:
                dayPieces = arguments.date.split('/')
                print arguments.date
                print dayPieces
                day = int(dayPieces[1])
                month = int(dayPieces[0])
                year = int(dayPieces[2])

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
            text = tk.Text(root, height=50, width=130)
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
            header = "Line\t   Date\t\t     " + relativeHumidityTitle + "\t\t\t\t      " + temperatureTitle \
                     + "\t\t\t\t   Vapor Pressure Deficit (kPa)\n"
            headerLineBreak = "------------------------------------------------------------------------------------" \
                              + "----------------------------------------------\n"
            text.insert(tk.END, header)
            text.insert(tk.END, headerLineBreak)
        else:
            header = "Line\t   Date\t\t\t " + relativeHumidityTitle + "\t\t  " + temperatureTitle \
                     + "\t\tVapor Pressure Deficit (kPa)\n"
            headerLineBreak = "------------------------------------------------------------------------------------" \
                              + "----------------\n"
            print(header)
            print(headerLineBreak)
        recordCount = 0  # found record count
        i = 21  # line count
        for date, relativeHumidity, temp in zip(dates, relativeHumidityData, temperatureData):
            if (date[0] == year and date[1] == month and date[2] == day) or showAll:
                # Check for No Data flag and convert printout if found, otherwise calculate VPD
                if float(temp) == -6999 or float(relativeHumidity) == -6999:
                    vpd = "No Data"
                    if float(temp) == -6999:
                        temp = "No Data"
                    if float(relativeHumidity) == -6999:
                        relativeHumidity = "No Data"
                else:
                    vpd = getVPD(float(temp), float(relativeHumidity))
                    vpd = sc_Pressure.pascalsTo_kiloPascals(vpd)
                    relativeHumidity = "{0:0.2f}".format(float(relativeHumidity))
                    if float(temp) < 0:
                        temp = "{0:0.3f}".format(float(temp))
                    else:
                        temp = " {0:0.3f}".format(float(temp))
                    vpd = "{0:0.2f}".format(float(vpd))  # Limits VPD to 2 decimals outside of speedcalc for formatting

                # Set up printout line
                if gui:
                    tabs = "\t"
                else:
                    if i < 100:
                        tabs = "\t\t"
                    else:
                        tabs = "\t"
                outputLine = str(i) + "." + tabs + time.strftime('%m/%d/%Y', date) + "\t\t\tRH: " + relativeHumidity +\
                    "\t\t\t\tT: " + temp + "\t\t\t\t=> VPD: " + str(vpd) + "\n"

                # Print to GUI or console depending on how program is run
                if gui:
                    text.insert(tk.END, outputLine)
                else:
                    print outputLine,
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
