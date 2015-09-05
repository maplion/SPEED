# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:29:58 2015

@author: Ryan Dammrose aka MapLion
"""

class Convert(object): #superclass, inherits from default object
    """
    Class for making conversions of different types.
    """

    def __init__(self):
        """
        The Constructor
        """
        pass

#############################################################################################################
class Length(Convert): #subclass, inherits from Convert
    """
    Subclass for Length created for the purpose
    of organization within the Convert superclass;
    These are conversions commonly used for Length calculations.
    """

    def __init__(self, printFormula="false", numberOfDecimals=6):
        """
        Initializes superclass Convert
        """
        super(Convert, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._printFormula = printFormula

    def meterToMillimeter(self, meters):
        """
        Converts meters to millimeters

        @param meters: Number of meters

        @returns: Number of millimeters

        Formula:
            Number of meters * 1000 = Number of millimeters
        """
        self._meters = meters
        _result = self._meters * 1000.0
        if self._printFormula == "true":
            print ("{1:{0}} m * 1000.0 = {2:{0}} mm".format(self._df, self._meters, _result))
        return _result

    def millimeterToMeter(self, millimeters):
        """
        Converts millimeters to meters

        @param millimeters: Number of millimeters

        @returns: Number of meters

        Formula:
            Number of millimeters / 1000 = Number of meters
        """
        self._millimeters = millimeters
        _result = self._millimeters / 1000.0
        if self._printFormula == "true":
            print ("{1:{0}} m / 1000.0 = {2:{0}} mm".format(self._df, self._millimeters, _result))
        return _result

#############################################################################################################
class Time(Convert): #subclass, inherits from Convert
    """
    Subclass for Time created for the purpose
    of organization within the Convert superclass;
    These are conversions commonly used for Time calculations.
    """

    def __init__(self, printFormula="false", numberOfDecimals=6):
        """
        Initializes superclass Convert

        @param numberOfDecimals: number of decimals when printing formulas
        """
        super(Convert, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._printFormula = printFormula

    def secondToMinute(self, seconds):
        """
        Converts seconds to minutes

        @param seconds: Number of seconds

        @returns: Number of minutes

        Formula:
            Number of seconds / 60 = Number of minutes
        """
        self._seconds = seconds
        _result = self._seconds / 60.0
        if self._printFormula == "true":
            print ("{1:{0}} s / 60.0 = {2:{0}} min".format(self._df, seconds, _result))
        return _result

    def minuteToSecond(self, minutes):
        """
        Converts minutes to seconds

        @param minutes: Number of minutes

        @returns: Number of seconds

        Formula:
            Number of minutes * 60 = Number of seconds
        """
        self._minutes = minutes
        _result = self._minutes * 60.0
        if self._printFormula == "true":
            print ("{1:{0}} min * 60.0 = {2:{0}} s".format(self._df, self._minutes, _result))
        return _result

    def minuteToHour(self, minutes):
        """
        Converts minutes to hours

        @param minutes: Number of minutes

        @returns: Number of hours

        Formula:
            Number of minutes / 60 = Number of hours
        """
        self._minutes = minutes
        _result = self._minutes / 60.0
        if self._printFormula == "true":
            print ("{1:{0}} min / 60.0 = {2:{0}} hr".format(self._df, self._minutes, _result))
        return _result

    def hourToMinute(self, hours):
        """
        Converts hours to minutes

        @param hours: Number of hours

        @returns: Number of minutes

        Formula:
            Number of hours * 60 = Number of minutes
        """
        self._hours = hours
        _result = self._hours * 60.0
        if self._printFormula == "true":
            print ("{1:{0}} min * 60.0 = {2:{0}} min".format(self._df, self._hours, _result))
        return _result

    def secondToHour(self, seconds):
        """
        Converts seconds to hours

        @param seconds: Number of seconds

        @returns: Number of hours

        Formula:
            Number of seconds / 3600 = Number of Hours
        """
        self._seconds = seconds
        _result = self._seconds / 3600.0
        if self._printFormula == "true":
            print ("{1:{0}} s / 3600.0 = {2:{0}} hr".format(self._df, self._seconds, _result))
        return _result


    def hourToSecond(self, hours):
        """
        Converts hours to seconds

        @param hours: Number of hours

        @returns: Number of seconds

        Formula:
            Number of hours * 3600 = Number of seconds
        """
        self._hours = hours
        _result = self._hours * 3600.0
        if self._printFormula == "true":
            print ("{1:{0}} hr * 3600.0 = {2:{0}} s".format(self._df, self._hours, _result))
        return _result

#############################################################################################################
class ET(Convert): #subclass, inherits from Convert
    """
    Subclass for evapotranspiration(ET) created for the purpose
    of organization within the Convert superclass;
    These are conversions commonly used for ET calculations.
    """

    def __init__(self, printFormula="false", numberOfDecimals=6):
        """
        Initializes superclass Convert
        """
        super(Convert, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._printFormula = printFormula
        
    def energyFluxToWaterEvaporated(self, energyFluxValue, waterDensity=1000.0):
        """
        Converts the values of evapotranspiration (ET) given in units of
        energy flux (W/m^2) to units of equivalent depth of water
        evaporated per day (mm/day)
        
        @param energyFluxValue: mass flux rate in kg/(m^2*s) [W/m^2]
        @param waterDensity: density value for water; defaults to 1000 kg/m^3
            
        @returns: Amount of Water Evaporated (in mm/day)
        
        Formula: 
        """
        self._energyFluxValue = energyFluxValue
        self._rho = waterDensity #Density of water in kg/m^3
        
        
