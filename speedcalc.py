#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scientific Programming for Earth and Ecological Discovery (SPEED) Calculation module created for the class.

This contains the core calculations and code for all SPEED Modules.

Note: As there are far more advanced [further abstraction, more dynamic, more feature-rich] libraries out there
for unit conversion, this was just done as an exercise to familiarize myself with certain constructs
that I am used to from other languages (e.g. Java/C#), help meet specific needs for a class and get
general practice at making something from scratch.

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import math

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"


class SpeedCalc(object):  # superclass, inherits from default object
    """
    Class for making conversions of different types.
    """

    def __init__(self):
        """
        The Constructor
        """
        pass
#############################################################################################################


class Length(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Length created for the purpose
    of organization within the SpeedCalc superclass;
    These are conversions commonly used for Length calculations.
    """

    def __init__(self, formula="false", numberOfDecimals=6):
        """
        Initializes subclass Length
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = numberOfDecimals

        # Initialize Instance Attributes that are used later
        self._meters = 'None'
        self._millimeters = 'None'

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
        if self._formula == "true":
            print ("{1:{0}} m * 1000.0 = {2:{0}} mm".format(self._df, self._meters, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} m / 1000.0 = {2:{0}} mm".format(self._df, self._millimeters, _result))
        return round(_result, self._numberOfDecimals)
#############################################################################################################


class Time(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Time created for the purpose
    of organization within the SpeedCalc superclass;
    These are conversions commonly used for Time calculations.
    """

    def __init__(self, formula="false", numberOfDecimals=6):
        """
        Initializes subclass Time

        @param numberOfDecimals: number of decimals when printing formulas
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = numberOfDecimals

        # Initialize Instance Attributes that are used later
        self._seconds = 'None'
        self._minutes = 'None'
        self._hours = 'None'
        self._days = 'None'

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
        if self._formula == "true":
            print ("{1:{0}} s / 60.0 = {2:{0}} min".format(self._df, seconds, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} min * 60.0 = {2:{0}} s".format(self._df, self._minutes, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} min / 60.0 = {2:{0}} hr".format(self._df, self._minutes, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} min * 60.0 = {2:{0}} min".format(self._df, self._hours, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} s / 3600.0 = {2:{0}} hr".format(self._df, self._seconds, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} hr * 3600.0 = {2:{0}} s".format(self._df, self._hours, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} s / 86400.0 = {2:{0}} days".format(self._df, self._seconds, _result))
        return round(_result, self._numberOfDecimals)

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
        if self._formula == "true":
            print ("{1:{0}} days * 86400.0 = {2:{0}} s".format(self._df, self._days, _result))
        return round(_result, self._numberOfDecimals)
#############################################################################################################


class ET(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for evapotranspiration(ET) created for the purpose
    of organization within the SpeedCalc superclass;
    These are conversions commonly used for ET calculations.
    """

    def __init__(self, formula="false", numberOfDecimals=6):
        """
        Initializes subclass ET
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = numberOfDecimals

        # Initialize Instance Attributes that are used later
        self._energyFluxValue = 'None'
        self._massFluxValue = 'None'
        self._waterDensity = 'None'

    def energyFluxToWaterEvaporated(self, energyFluxValue, waterDensity=1000.0):
        """
        Converts the values of evapotranspiration (ET) given in units of
        energy flux (W/m^2) to units of equivalent depth of water
        evaporated per day (mm/day).

        In other words, it is a conversion of the evaporation of water in units of
        power per unit area of earth surface to volume of water evaporated per unit area
        of earth surface, per unit time.

        @param energyFluxValue: energy flux rate in W/m^2
        @param waterDensity: density value for water; defaults to 1000 kg/m^3
            
        @returns: Amount of Water Evaporated (in mm/day)
        
        Formula::
            (energyFluxValue W/m^2 * 1 J/s * 3600 s * 24 hr * 1000 mm)/(2.26E6 J/kg * waterDensity kg)
        OR  massFluxValue kg/(m^2*s) / 2.26E6 J
        """
        self._energyFluxValue = energyFluxValue
        self._waterDensity = waterDensity  # Density of water in kg/m^3
        _result = ((self._energyFluxValue * 3600.0 * 24.0 * 1000) / (2.26e6 * self._waterDensity))
        if self._formula == "true":
            print ("({1:{0}} W/m^2 * 1 J/s * 3600 s * 24 hr * 1000 mm)/(2.26E6 J/kg * {3} kg "
                   "= {2:{0}} mm/day".format(self._df, self._energyFluxValue, _result, self._waterDensity))
        return round(_result, self._numberOfDecimals)

    def massFluxToWaterEvaporated(self, massFluxValue, waterDensity=1000.0):
        """
        Converts the values of evapotranspiration (ET) given in mass flux
        units of kg/(m^2*s) to units of equivalent depth of water
        evaporated per day in mm/day.

        @param massFluxValue: mass flux rate in kg/(m^2*s)
        @param waterDensity: density value for water; defaults to 1000 kg/m^3

        @returns: Amount of Water Evaporated in mm/day

        Formula::
            massFluxValue * (1.0/waterDensity) * 1000 * 3600 * 24
        """
        self._massFluxValue = massFluxValue
        self._waterDensity = waterDensity  # Density of water in kg/m^3
        _result = self._massFluxValue * (1.0/self._waterDensity) * 1000 * 3600 * 24
        if self._formula == "true":
            print ("({1:{0}} [kg/(m^2*s)] / {3} [kg/m^3]) * 1000 mm * 3600 s * 24 hr "
                   "= {2:{0}} mm/day".format(self._df, self._massFluxValue, _result, self._waterDensity))
        return round(_result, self._numberOfDecimals)
#############################################################################################################


class Pressure(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Pressure created for the purpose
    of organization within the SpeedCalc superclass;
    These are conversions commonly used for Pressure calculations.
    """

    def __init__(self, formula="false", numberOfDecimals=6):
        """
        Initializes subclass Pressure
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(numberOfDecimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = numberOfDecimals

        # Initialize Instance Attributes that are used later
        self._units = 'None'
        self._T = 'None'
        self._phase = 'None'

    def saturationVaporPressure(self, temperatureCelsius, phase="liquid", units="Pa"):
        """
        Calculates Saturation Vapor Pressure from a given Temperature in Celsius.

        @param temperatureCelsius: Degrees Celsius
        @param phase: takes "liquid" and "ice" as parameters; defaults to "liquid"
        @param units: takes "Pa", "hPa", and "kPa"; defaults to "Pa"
        @return: saturation vapor pressure (e*) in Pascals (Pa)
        """
        self._units = units
        self._T = temperatureCelsius
        self._phase = phase
        if self._phase == "ice":
            _CONST1 = 21.87
            _CONST2 = 265.5
            _eStar = 611.0 * math.exp((_CONST1 * self._T)/(self._T + _CONST2))
        else:
            _CONST1 = 17.27
            _CONST2 = 237.3
            _eStar = 611.0 * math.exp((_CONST1 * self._T)/(self._T + _CONST2))
        if self._units.lower() == "kpa":
            _eStar /= 1000.0
        elif self._units.lower() == "hpa":
            _eStar /= 100.0
        _result = _eStar
        if self._formula == "true":
            print ("Phase: {5}\n611.0 * exp(({2} * {1} [C])/({1} [C] + {3}) = {6:{0}} [{4}]".format(
                self._df, self._T, _CONST1, _CONST2, self._units, phase, _result))
        return round(_result, self._numberOfDecimals)  # Saturation Vapor Pressure
