# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:29:58 2015

@author: Ryan Dammrose aka MapLion

Note: As there are far more advanced [further abstraction, more dynamic, more feature-rich] libraries out there
for unit conversion, this was just done as an exercise to familiarize myself with certain constructs
that I am used to from other languages (e.g. Java/C#), help meet specific needs for a class and get
general practice at making something from scratch.
"""

import math

class Convert(object):  # superclass, inherits from default object
    """
    Class for making conversions of different types.
    """

    def __init__(self):
        """
        The Constructor
        """
        pass

#############################################################################################################
class Length(Convert):  # subclass, inherits from Convert
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

        Formula::
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

        Formula::
            Number of millimeters / 1000 = Number of meters
        """
        self._millimeters = millimeters
        _result = self._millimeters / 1000.0
        if self._printFormula == "true":
            print ("{1:{0}} m / 1000.0 = {2:{0}} mm".format(self._df, self._millimeters, _result))
        return _result

#############################################################################################################
class Time(Convert):  # subclass, inherits from Convert
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

        Formula::
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

        Formula::
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

        Formula::
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

        Formula::
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

        Formula::
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

        Formula::
            Number of hours * 3600 = Number of seconds
        """
        self._hours = hours
        _result = self._hours * 3600.0
        if self._printFormula == "true":
            print ("{1:{0}} hr * 3600.0 = {2:{0}} s".format(self._df, self._hours, _result))
        return _result

    def secondToDay(self, seconds):
        """
        Converts seconds to days

        @param seconds: Number of seconds

        @returns: Number of days

        Formula::
            Number of seconds / 86400 = Number of days
        """
        self._seconds = seconds
        _result = self._seconds / 86400.0
        if self._printFormula == "true":
            print ("{1:{0}} s / 86400.0 = {2:{0}} days".format(self._df, self._seconds, _result))
        return _result

    def dayToSecond(self, days):
        """
        Converts days to seconds

        @param days: Number of days

        @returns: Number of seconds

        Formula::
            Number of days * 86400 = Number of seconds
        """
        self._days = days
        _result = self._days * 86400.0
        if self._printFormula == "true":
            print ("{1:{0}} days * 86400.0 = {2:{0}} s".format(self._df, self._days, _result))
        return _result

#############################################################################################################
class ET(Convert):  # subclass, inherits from Convert
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
        
        @param energyFluxValue: mass flux rate in kg/(m^2*s)
        @param waterDensity: density value for water; defaults to 1000 kg/m^3
            
        @returns: Amount of Water Evaporated (in mm/day)
        
        Formula::
            Long route:
            1 W/m^2 = 1 J/(s*m^2)
            1 J/(s*m^2) = 1 N/(m*s)
            1 MegaJoule = 1000000 * 1 N/(m*s)
            TODO:
            MegaJoules conversion factor: 1 mm/day = 2.45 MJ*m^(-2)/day
            energyFluxValue conversion factor: 1 Wm^(-2) = 0.0864 MJ*m^(-2)/day
            conversion factor = 2.45 MJ m^(-2)/day / 0.0864 0.0864 MJ*m^(-2)/day = ~28.35648148
            waterEvaporated = energyFluxValue / conversion factor
        """
        self._ET_ef = energyFluxValue
        self._rho = waterDensity  # Density of water in kg/m^3
        _result = (self._ET_ef / (28.35648148/self._rho*1000))
        if self._printFormula == "true":
            print ("({1:{0}} W/m^2 / (28.35648148/waterDensity*1000)) = {2:{0}} mm/day".format(self._df, self._ET_ef, _result))
        return _result

    def massFluxToWaterEvaporated(self, massFluxValue, waterDensity=1000.0):
        """
        Converts the values of evapotranspiration (ET) given in mass flux
        units of kg/(m^2*s) to units of equivalent depth of water
        evaporated per day in mm/day

        @param massFluxValue: mass flux rate in kg/(m^2*s)
        @param waterDensity: density value for water; defaults to 1000 kg/m^3

        @returns: Amount of Water Evaporated in mm/day

        Formula::
            massFluxValue * (1.0/waterDensity) * 1000 * 3600 * 24
        """
        self._ET_mf = massFluxValue
        self._rho = waterDensity  # Density of water in kg/m^3
        _result = self._ET_mf * (1.0/self._rho) * 1000 * 3600 * 24
        if self._printFormula == "true":
            print ("({1:{0}} [kg/(m^2*s)] / {3} [kg/m^3]) * 1000 mm * 3600 s * 24 hr = {2:{0}} mm/day".format(self._df, self._ET_mf, _result, self._rho))
        return _result

#############################################################################################################
class Pressure(Convert):  # subclass, inherits from Convert
    """
    Subclass for Pressure created for the purpose
    of organization within the Convert superclass;
    These are conversions commonly used for Pressure calculations.
    """

    def __init__(self, printFormula="false", numberOfDecimals=6):
        """
        Initializes superclass Convert
        """
        super(Convert, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._printFormula = printFormula


    def saturationVaporPressure(self, temperatureCelsius, waterPhase="liquid", resultPascal="Pa"):
        """
        Calculates Saturation Vapor Pressure from a given Temperature in Celsius.
        
        @param temperatureCelsius: Degrees Celsius
        @param waterPhase: takes "liquid" and "ice" as parameters; defaults to "liquid"
        @param resultPascal: takes "Pa", "hPa", and "kPa"; defaults to "Pa"
        @return: saturation vapor pressure (e*) in Pascals (Pa)
        """
        self._resultPascal = resultPascal.lower()
        self._T = temperatureCelsius
        if waterPhase == "ice":
            _const1 = 21.87
            _const2 = 265.5
            _eStar = 611.0 * math.exp((_const1 * self._T)/(self._T + _const2))
        else:
            _const1 = 17.27
            _const2 = 237.3
            _eStar = 611.0 * math.exp((_const1 * self._T)/(self._T + _const2))
        if resultPascal == "kpa":
            _eStar = _eStar / 1000.0
        elif resultPascal == "hpa":
            _eStar = _eStar / 100.0
        _result = _eStar
        if self._printFormula == "true":
            print ("611.0 * exp(({2} * {1} [C])/({1} [C] + {3}) = {4:{0}} [Pa]".format(self._df, self._T, _const1, _const2, _result))
        return _result  # Saturation Vapor Pressure
