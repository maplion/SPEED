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
import numpy
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
import pysal

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"


class SpeedCalc(object):  # superclass, inherits from default object
    """
    Class for making conversions of different types.
    """
    # TODO: Rebuild Conversions

    def __init__(self):
        """
        The Constructor
        """
        self._inputString = None

    def is_integer(self, string):
        """
        Checks if a string is an integer.
        @param string: integer as a string
        @returns: True if it is an integer and False if it is not
        """
        try:
            self._inputString = string
            int(string)
            return True
        except ValueError:
            return False
#############################################################################################################


class Length(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Length created for the purpose
    of organization within the SpeedCalc superclass;
    These are conversions commonly used for Length calculations.
    """

    def __init__(self, formula=False, number_of_decimals=6):
        """
        Initializes subclass Length
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self._meters = None
        self._millimeters = None

    def meter_to_millimeter(self, meters):
        """
        Converts meters to millimeters

        @param meters: Number of meters

        @returns: Number of millimeters

        Formula::
            Number of meters * 1000 = Number of millimeters
        """
        self._meters = meters
        _result = self._meters * 1000.0
        if self._formula:
            print ("{1:{0}} m * 1000.0 = {2:{0}} mm".format(self._df, self._meters, _result))
        return round(_result, self._numberOfDecimals)

    def millimeter_to_meter(self, millimeters):
        """
        Converts millimeters to meters

        @param millimeters: Number of millimeters

        @returns: Number of meters

        Formula::
            Number of millimeters / 1000 = Number of meters
        """
        self._millimeters = millimeters
        _result = self._millimeters / 1000.0
        if self._formula:
            print ("{1:{0}} m / 1000.0 = {2:{0}} mm".format(self._df, self._millimeters, _result))
        return round(_result, self._numberOfDecimals)
#############################################################################################################


class Time(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Time created for the purpose
    of organization within the SpeedCalc superclass;
    These are conversions commonly used for Time calculations.
    """

    def __init__(self, formula=False, number_of_decimals=6):
        """
        Initializes subclass Time

        @param number_of_decimals: number of decimals when printing formulas
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self._seconds = None
        self._minutes = None
        self._hours = None
        self._days = None

    def second_to_minute(self, seconds):
        """
        Converts seconds to minutes

        @param seconds: Number of seconds

        @returns: Number of minutes

        Formula::
            Number of seconds / 60 = Number of minutes
        """
        self._seconds = seconds
        _result = self._seconds / 60.0
        if self._formula:
            print ("{1:{0}} s / 60.0 = {2:{0}} min".format(self._df, seconds, _result))
        return round(_result, self._numberOfDecimals)

    def minute_to_second(self, minutes):
        """
        Converts minutes to seconds

        @param minutes: Number of minutes

        @returns: Number of seconds

        Formula::
            Number of minutes * 60 = Number of seconds
        """
        self._minutes = minutes
        _result = self._minutes * 60.0
        if self._formula:
            print ("{1:{0}} min * 60.0 = {2:{0}} s".format(self._df, self._minutes, _result))
        return round(_result, self._numberOfDecimals)

    def minute_to_hour(self, minutes):
        """
        Converts minutes to hours

        @param minutes: Number of minutes

        @returns: Number of hours

        Formula::
            Number of minutes / 60 = Number of hours
        """
        self._minutes = minutes
        _result = self._minutes / 60.0
        if self._formula:
            print ("{1:{0}} min / 60.0 = {2:{0}} hr".format(self._df, self._minutes, _result))
        return round(_result, self._numberOfDecimals)

    def hour_to_minute(self, hours):
        """
        Converts hours to minutes

        @param hours: Number of hours

        @returns: Number of minutes

        Formula::
            Number of hours * 60 = Number of minutes
        """
        self._hours = hours
        _result = self._hours * 60.0
        if self._formula:
            print ("{1:{0}} min * 60.0 = {2:{0}} min".format(self._df, self._hours, _result))
        return round(_result, self._numberOfDecimals)

    def second_to_hour(self, seconds):
        """
        Converts seconds to hours

        @param seconds: Number of seconds

        @returns: Number of hours

        Formula::
            Number of seconds / 3600 = Number of Hours
        """
        self._seconds = seconds
        _result = self._seconds / 3600.0
        if self._formula:
            print ("{1:{0}} s / 3600.0 = {2:{0}} hr".format(self._df, self._seconds, _result))
        return round(_result, self._numberOfDecimals)

    def hour_to_second(self, hours):
        """
        Converts hours to seconds

        @param hours: Number of hours

        @returns: Number of seconds

        Formula::
            Number of hours * 3600 = Number of seconds
        """
        self._hours = hours
        _result = self._hours * 3600.0
        if self._formula:
            print ("{1:{0}} hr * 3600.0 = {2:{0}} s".format(self._df, self._hours, _result))
        return round(_result, self._numberOfDecimals)

    def second_to_day(self, seconds):
        """
        Converts seconds to days

        @param seconds: Number of seconds

        @returns: Number of days

        Formula::
            Number of seconds / 86400 = Number of days
        """
        self._seconds = seconds
        _result = self._seconds / 86400.0
        if self._formula:
            print ("{1:{0}} s / 86400.0 = {2:{0}} days".format(self._df, self._seconds, _result))
        return round(_result, self._numberOfDecimals)

    def day_to_second(self, days):
        """
        Converts days to seconds

        @param days: Number of days

        @returns: Number of seconds

        Formula::
            Number of days * 86400 = Number of seconds
        """
        self._days = days
        _result = self._days * 86400.0
        if self._formula:
            print ("{1:{0}} days * 86400.0 = {2:{0}} s".format(self._df, self._days, _result))
        return round(_result, self._numberOfDecimals)
#############################################################################################################


class ET(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for evapotranspiration(ET) created for the purpose
    of organization within the SpeedCalc superclass;
    These are conversions commonly used for ET calculations.
    """

    def __init__(self, formula=False, number_of_decimals=6):
        """
        Initializes subclass ET
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self._energyFluxValue = None
        self._massFluxValue = None
        self._waterDensity = None

    def energy_flux_to_water_evaporated(self, energy_flux_value, water_density=1000.0):
        """
        Converts the values of evapotranspiration (ET) given in units of
        energy flux (W/m^2) to units of equivalent depth of water
        evaporated per day (mm/day).

        In other words, it is a conversion of the evaporation of water in units of
        power per unit _area of earth surface to volume of water evaporated per unit _area
        of earth surface, per unit time.

        @param energy_flux_value: energy flux rate in W/m^2
        @param water_density: density value for water; defaults to 1000 kg/m^3

        @returns: Amount of Water Evaporated (in mm/day)

        Formula::
            (energy_flux_value W/m^2 * 1 J/s * 3600 s * 24 hr * 1000 mm)/(2.26E6 J/kg * water_density kg)
        OR  massFluxValue kg/(m^2*s) / 2.26E6 J
        """
        self._energyFluxValue = energy_flux_value
        self._waterDensity = water_density  # Density of water in kg/m^3
        _result = ((self._energyFluxValue * 3600.0 * 24.0 * 1000) / (2.26e6 * self._waterDensity))
        if self._formula:
            print ("({1:{0}} W/m^2 * 1 J/s * 3600 s * 24 hr * 1000 mm)/(2.26E6 J/kg * {3} kg "
                   "= {2:{0}} mm/day".format(self._df, self._energyFluxValue, _result, self._waterDensity))
        return round(_result, self._numberOfDecimals)

    def mass_flux_to_water_evaporated(self, mass_flux_value, water_density=1000.0):
        """
        Converts the values of evapotranspiration (ET) given in mass flux
        units of kg/(m^2*s) to units of equivalent depth of water
        evaporated per day in mm/day.

        @param mass_flux_value: mass flux rate in kg/(m^2*s)
        @param water_density: density value for water; defaults to 1000 kg/m^3

        @returns: Amount of Water Evaporated in mm/day

        Formula::
            mass_flux_value * (1.0/water_density) * 1000 * 3600 * 24
        """
        self._massFluxValue = mass_flux_value
        self._waterDensity = water_density  # Density of water in kg/m^3
        _result = self._massFluxValue * (1.0/self._waterDensity) * 1000 * 3600 * 24
        if self._formula:
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

    def __init__(self, formula=False, number_of_decimals=6):
        """
        Initializes subclass Pressure

        @param formula: set formula to true to have the calculations print the formulas as they are calculated
        @param number_of_decimals: sets the number of decimals the result values will return
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self._T = None
        self._relativeHumidity = None
        self._saturationVaporPressure = None
        self._vaporPressure = None
        self._pascalValue = None
        self._multiplier = None
        self._units = None

    def vapor_pressure_from_temperature(self, temperature, units="Pa"):
        """
        Calculates Vapor Pressure from a given Temperature in Celsius.
        For Saturation Vapor Pressure, put in the temperature.
        For actual vapor Pressure, enter the Dewpoint Temperature.

        @param temperature: Degrees Celsius
        @param units: display units; defaults in Pa
        @return: saturation vapor pressure (e*) in Pascals (Pa)

        Formula::
            liquid:
            611.0 * exp(temperature * 17.27)/(temperature + 237.3)  [Pa]
        """
        self._T = temperature
        self._units = units

        if self._T < 0:
            _phase = "ice"
            _CONST1 = 21.87
            _CONST2 = 265.5
            _eStar = 611.0 * math.exp((_CONST1 * self._T)/(self._T + _CONST2))
        else:
            _phase = "liquid"
            _CONST1 = 17.27
            _CONST2 = 237.3
            _eStar = 611.0 * math.exp((_CONST1 * self._T)/(self._T + _CONST2))

        _result = _eStar
        if self._formula:
            print ("Phase: {5}\n611.0 * exp(({2} * {1} [C])/({1} [C] + {3}) = {6:{0}} [{4}]".format(
                self._df, self._T, _CONST1, _CONST2, self._units, _phase, _result))
        return round(_result, self._numberOfDecimals)

    def relative_humidity(self, vapor_pressure, saturation_vapor_pressure, units="Pa"):
        """
        Calculates the relative humidity from the vapor pressure (e) and saturation vapor pressure (e*)

        @param vapor_pressure:  The vapor pressure (e) in Pa
        @param saturation_vapor_pressure: The saturation vapor pressure (e*) in Pa
        @param units: display units; defaults in Pa
        @return: returns the relative humidity

        Formula::
            relative_humidity = vapor_pressure/saturation_vapor_pressure
        """
        self._vaporPressure = vapor_pressure
        self._saturationVaporPressure = saturation_vapor_pressure
        self._units = units

        _relativeHumidity = self._vaporPressure / self._saturationVaporPressure

        _result = _relativeHumidity
        if self._formula:
            print ("{1} / {2} = {3:{0}} [{4}]".format(
                self._df, self._vaporPressure, self._saturationVaporPressure, _result, self._units))
        return round(_result, self._numberOfDecimals)

    def vapor_pressure_from_relative_humidity(self, relative_humidity, saturation_vapor_pressure, units="Pa"):
        """
        Calculates the vapor pressure using the relative humidity equation.

        @param relative_humidity:  The relative humidity value in decimal form (e.g. 50% => 0.5) [divides by 100 if not]
        @param saturation_vapor_pressure: The saturation vapor pressure (often symbolized as "e*") in Pa
        @param units: display units; defaults in Pa
        @return: returns the vapor pressure in Pa

        Formula::
            vapor_pressure_from_relative_humidity = relative_humidity * saturation_vapor_pressure
        """
        self._relativeHumidity = relative_humidity
        self._saturationVaporPressure = saturation_vapor_pressure
        self._units = units

        if self._relativeHumidity > 1:
            self._relativeHumidity /= 100.0

        _vaporPressure = self._relativeHumidity * self._saturationVaporPressure

        _result = _vaporPressure
        if self._formula:
            print ("{1} * {2} = {3:{0}} [{4}]".format(
                self._df, self._relativeHumidity, self._saturationVaporPressure, _result, self._units))
        return round(_result, self._numberOfDecimals)

    def vapor_pressure_deficit(self, saturation_vapor_pressure, vapor_pressure, units="Pa"):
        """
        Calculates the vapor pressure deficit (VPD).

        @param saturation_vapor_pressure: The saturation vapor pressure (e*) in Pa
        @param vapor_pressure: The vapor pressure (e) in Pa
        @param units: display units; defaults in Pa
        @return: returns the vapor pressure deficit in Pa

        Formula::
            vapor_pressure_deficit = saturation_vapor_pressure - vapor_pressure
        """
        self._saturationVaporPressure = saturation_vapor_pressure
        self._vaporPressure = vapor_pressure
        self._units = units

        _vaporPressureDeficit = self._saturationVaporPressure - self._vaporPressure

        _result = _vaporPressureDeficit
        if self._formula:
            print ("{1} - {2} = {3:{0}} [{4}]".format(
                self._df, self._saturationVaporPressure, self._vaporPressure, _result, self._units))
        return round(_result, self._numberOfDecimals)

    def pascals_to_kilopascals(self, pascal_value):
        """
        Converts pascals to kilopascals [kPa]

        @param pascal_value: the pascal value to convert

        Formula::
            0.001 * pascal_value = kiloPascals
        """
        self._units = "kPa"
        self._multiplier = 0.001
        self._pascalValue = pascal_value
        _result = self._multiplier * self._pascalValue
        if self._formula:
            print ("{1} * {2} = {3:{0}} [{4}]".format(
                self._df, self._multiplier, self._pascalValue, _result, self._units))
        return round(_result, self._numberOfDecimals)

    def pascals_to_hectopascals(self, pascal_value):
        """
        Converts pascals to hectopascals [hPa]

        @param pascal_value: the pascal value to convert

        Formula::
            0.01 * pascal_value = kiloPascals
        """
        self._units = "hPa"
        self._multiplier = 0.01
        self._pascalValue = pascal_value
        _result = self._multiplier * self._pascalValue
        if self._formula:
            print ("{1} * {2} = {3:{0}} [{4}]".format(
                self._df, self._multiplier, self._pascalValue, _result, self._units))
        return round(_result, self._numberOfDecimals)

    def dew_point_temperature(self, vapor_pressure):
        """
        Calculates the dew point temperature from the given vapor pressure

        @param vapor_pressure: the actual vapor pressure [at a given temperature]
        @return: dew point temperature

        Formula::
            dewPoint = (ln(vapor_pressure) - 6.415)/(0.0999-0.00421 * ln(vapor_pressure))
        """
        self._vaporPressure = vapor_pressure

        _result = (math.log1p(vapor_pressure) - 6.415) / (0.0999 - 0.00421 * math.log1p(vapor_pressure))
        if self._formula:
            print ("(ln({1}) - 6.415)/(0.0999-0.00421 * ln({1})) = {2:{0}} [Celsius]".format(
                self._df, self._vaporPressure, _result))
        return _result


class Polygon(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Polygon, created for Module 09.
    """

    def __init__(self, x_coords, y_coords, formula=False, number_of_decimals=6):
        """
        Initializes subclass Polygon
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self._x_coords = None
        self._y_coords = None
        self._area = None
        self._centroid_x = None
        self._centroid_y = None
        self._perimeter = None

        # Validate polygon coordinates
        self.validate_polygon(x_coords, y_coords)

        # Set area, centroid, and perimeter of polygon
        self.set_poly_area()
        self.set_poly_centroid()
        self.set_poly_perimeter()

    def validate_polygon(self, x_coords, y_coords):
        """
        Checks if coordinates given make a valid polygon by summing the coordinates and seeing if they are equal.

        @param x_coords: x coordinates of Polygon
        @param y_coords: y coordinates of Polygon
        """
        self._x_coords = x_coords
        self._y_coords = y_coords

        try:
            if (numpy.sum(self._x_coords) != numpy.sum(self._y_coords)) or (len(self._x_coords) != len(self._y_coords)):
                raise ValueError("Invalid Polygon Coordinates Given (e.g. sum(x) does not equal sum(y), or number of"
                                 "coordinates for x and y does not match.")
        except ValueError as e:
            raise e

    def set_poly_area(self):
        """
        Calculates and sets Polygon Area
        """
        _calcSum = float(0)
        _last = len(self._x_coords)
        for i in range(len(self._x_coords)):
            p = (i+1) % _last             
            _calc = self._x_coords[i] * self._y_coords[p] - self._y_coords[i] * self._x_coords[p]
            _calcSum += _calc
            i += 1
        self._area = abs(_calcSum)/2.0

    def set_poly_centroid(self):
        """
        Calculates and sets Polygon Centroid (x, y)
        """
        _calcSum_x = float(0)
        _calcSum_y = float(0)
        _last = len(self._x_coords)
        for i in range(len(self._x_coords)):
            p = (i+1) % _last            
            _calc_x = (self._x_coords[i] + self._x_coords[p]) * \
                (self._x_coords[i] * self._y_coords[p] - self._x_coords[p] * self._y_coords[i])
            _calc_y = (self._y_coords[i] + self._y_coords[p]) * \
                (self._x_coords[i] * self._y_coords[p] - self._x_coords[p] * self._y_coords[i])
            _calcSum_x += _calc_x
            _calcSum_y += _calc_y
            i += 1
        self._centroid_x = (1.0/(6.0 * self._area)) * abs(_calcSum_x)
        self._centroid_y = (1.0/(6.0 * self._area)) * abs(_calcSum_y)

    def set_poly_perimeter(self):
        """
        Calculates and sets Polygon Perimeter
        """
        _calcSum = float(0)
        _last = len(self._x_coords)
        for i in range(len(self._x_coords)):
            p = (i+1) % _last
            _calc = (self._x_coords[p] - self._x_coords[i])**2 + (self._y_coords[p] - self._y_coords[i])**2
            _calcSum += math.sqrt(_calc)
            i += 1
        self._perimeter = _calcSum

    def get_poly_area(self):
        """
        Gets the Polygon Area
        @returns: Polygon Area
        """
        return round(self._area, self._numberOfDecimals)

    def get_poly_centroid(self):
        """
        Gets the Polygon Centroid
        @returns: Polygon Centroid
        """
        return round(self._centroid_x, self._numberOfDecimals), round(self._centroid_y, self._numberOfDecimals)

    def get_poly_perimeter(self):
        """
        Gets the Polygon Perimeter
        @returns: Polygon Perimeter
        """
        return round(self._perimeter, self._numberOfDecimals)


class RandomWalk(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Random Walking, created for Module 10.
    """

    def __init__(self, number_of_random_walkers, number_of_steps, average_step_size=1, std_in_step_size=2.5,
                 beginning_position=0, formula=False, number_of_decimals=6):
        """
        Initializes subclass Polygon
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self._numberOfRandomWalkers = number_of_random_walkers
        self._numberOfSteps = number_of_steps
        self._averageStepSize = average_step_size
        self._stdInStepSize = std_in_step_size
        self._beginningPosition = beginning_position

    def random_walk_1d(self):
        """
        One-dimensional simulation of random walkers

        @returns: Summed total of steps
        """
        _moves = numpy.random.normal(self._averageStepSize, self._stdInStepSize,
                                     size=self._numberOfSteps*self._numberOfRandomWalkers)
        _moves.shape = (self._numberOfSteps, self._numberOfRandomWalkers)
        _summed = numpy.zeros((self._numberOfSteps, self._numberOfRandomWalkers))

        # for step in range(self._numberOfSteps):
        #     this_move = _moves[step, :]
        #     _summed += numpy.where(this_move > 0, _moves[step, :], 0)

        # TODO: Try to figure out if there is a better, more vectorized way to do this if possible
        for j in range(self._numberOfRandomWalkers):
            for i in range(self._numberOfSteps):
                if i > 0:
                    _summed[i, j] = _summed[i-1, j] + _moves[i, j]
                else:
                    _summed[i, j] = _moves[i, j]

        _averageSteps = numpy.mean(_summed, axis=1)
        _totalSummed = numpy.vstack([numpy.zeros(self._numberOfRandomWalkers), _summed])

        return _totalSummed, _averageSteps

    # def randomWalk_2D(self):
    #     """
    #     Modified version of random 2D walk from "A Primer in Scientific Programming"
    #
    #     @returns x positions and y positions of random steps
    #     """
    #     _xpositions = numpy.zeros(self._numberOfRandomWalkers)
    #     _ypositions = numpy.zeros(self._numberOfRandomWalkers)
    #     _moves = numpy.random.random_integers(1, 4, size=self._numberOfSteps*self._numberOfRandomWalkers)
    #     _moves.shape = (self._numberOfSteps, self._numberOfRandomWalkers)
    #
    #     # Set Direction Constants
    #     _NORTH = 1
    #     _SOUTH = 2
    #     _WEST = 3
    #     _EAST = 4
    #
    #     for step in range(self._numberOfSteps):
    #         this_move = _moves[step, :]
    #         _ypositions += numpy.where(this_move == _NORTH, 1, 0)
    #         _ypositions -= numpy.where(this_move == _SOUTH, 1, 0)
    #         _xpositions += numpy.where(this_move == _EAST, 1, 0)
    #         _xpositions -= numpy.where(this_move == _WEST, 1, 0)
    #
    #     return _xpositions, _ypositions


class PlantWaterStress(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Plant Water Stress, created for Module 11 and Module 12.
    """

    def __init__(self, formula=False, number_of_decimals=6):
        """
        Initializes subclass Plant Water Stress
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self._soilMoistureData = None
        self._timeInterval = None
        self._waterMoisture = None

    # TODO: write test for this
    def calculate_pws(self, soil_moisture_data, change_in_time, water_moisture):
        """
        Calculates Plant Water Stress using trapezoidal rule

        @param soil_moisture_data: a list of soil moisture data
        @param change_in_time: the change in time
        @param water_moisture: the amount of water moisture
        @return: Plant Water Stress
        """
        self._soilMoistureData = soil_moisture_data
        self._timeInterval = change_in_time
        self._waterMoisture = water_moisture

        # TODO: Refactor
        # Convert soil_moisture_data List into an array
        _soilMoistureDataArray = numpy.asarray(self._soilMoistureData)
        _soilMoistureDataArray = _soilMoistureDataArray.astype(float)
        _results = numpy.zeros(_soilMoistureDataArray.size)

        it = numpy.nditer(_soilMoistureDataArray)
        it_ahead = numpy.nditer(_soilMoistureDataArray)
        it_ahead.iternext()
        range_start, range_end = it.iterrange
        range_end -= 1
        while it.iterindex < range_end:
            _results[it.iterindex] = 0.5 * self._timeInterval * \
                ((numpy.asscalar(it.value) - self._waterMoisture) +
                 (numpy.asscalar(it_ahead.value) - self._waterMoisture))
            it.iternext()
            it_ahead.iternext()
        _result = numpy.sum(_results)
        return _result

    def calculate_pws2(self, soil_moisture_data, time_interval):
        """
        Calculate PWS2 using centered difference

        @param soil_moisture_data: a list of soil moisture data
        @param time_interval: the time interval of the data
        @return: Plant Water Stress 2 array
        """
        self._soilMoistureData = soil_moisture_data
        self._timeInterval = time_interval

        # TODO: Refactor
        # Convert soil_moisture_data List into an array
        _soilMoistureDataArray = numpy.asarray(self._soilMoistureData)
        _soilMoistureDataArray = _soilMoistureDataArray.astype(float)
        _results = numpy.zeros(_soilMoistureDataArray.size - 2)

        it_behind = numpy.nditer(_soilMoistureDataArray)
        it = numpy.nditer(_soilMoistureDataArray)
        it_ahead = numpy.nditer(_soilMoistureDataArray)
        it_ahead.iternext()
        it_ahead.iternext()
        range_start, range_end = it.iterrange
        range_end -= 2
        while it.iterindex < range_end:
            _results[it.iterindex] = (numpy.asscalar(it_ahead.value) - numpy.asscalar(it_behind.value)) / \
                (2 * self._timeInterval)
            it.iternext()
            it_ahead.iternext()
            it_behind.iternext()
        return _results


class PredatorPrey(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for Lotka–Volterra equations and Predator Prey equations,
    created for Module 13
    """

    def __init__(self, prey_birth_rate_alpha, prey_death_rate_beta, predator_death_rate_gamma,
                 predator_birth_rate_delta, formula=False, number_of_decimals=6):
        """
        Initializes subclass PredatorPrey

        @param prey_birth_rate_alpha: Prey Birth Rate
        @param prey_death_rate_beta: Prey Death Rate
        @param predator_death_rate_gamma: Predator Death Rate
        @param predator_birth_rate_delta: Predator Birth Rate
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Parameters
        self._prey_birthRate_alpha = prey_birth_rate_alpha
        self._prey_deathRate_beta = prey_death_rate_beta
        self._predator_deathRate_gamma = predator_death_rate_gamma
        self._predator_birthRate_delta = predator_birth_rate_delta

        # Initialize Instance Attributes that are used later
        self._prey_initialPopulation = None
        self._predator_initialPopulation = None
        self._totalTime = None
        self._numberOfTimeSteps = None

    def lotka_volterra(self, prey_initial_population, predator_initial_population, total_time, number_of_time_steps):
        """

        @param prey_initial_population: The initial population value of the Prey
        @param predator_initial_population: The initial population value of the Predator
        @param total_time: Amount of total time within the model (total time divided by number of time steps
            determines number of iterations)
        @param number_of_time_steps: The number of total_time steps the total total_time will be divided by
        @return: Time Model Population Array of Predator, Prey, and total number of data points for plotting
        """
        self._prey_initialPopulation = prey_initial_population
        self._predator_initialPopulation = predator_initial_population
        self._totalTime = total_time
        self._numberOfTimeSteps = number_of_time_steps

        _changeInTime = self._totalTime/(float(self._numberOfTimeSteps))  # Set the change in time value
        _N1 = numpy.zeros(self._numberOfTimeSteps + 1)  # Create Zero array for Prey
        _N2 = numpy.zeros(self._numberOfTimeSteps + 1)  # Create Zero array for Predator
        _N1[0] = self._prey_initialPopulation  # Set initial value of prey population
        _N2[0] = self._predator_initialPopulation  # Set initial value for predator population
        _dataPointsForPlot = numpy.linspace(0, self._totalTime, self._numberOfTimeSteps + 1)

        # Calculate the Predator and Prey populations, iterated over increments within the given time total
        for i in range(self._numberOfTimeSteps):
            _N1[i+1] = _N1[i] + _changeInTime * ((self._prey_birthRate_alpha * _N1[i]) -
                                                 (self._prey_deathRate_beta * _N1[i] * _N2[i]))
            _N2[i+1] = _N2[i] + _changeInTime * ((self._predator_birthRate_delta * _N1[i] * _N2[i]) -
                                                 (self._predator_deathRate_gamma * _N2[i]))
        return _N1, _N2, _dataPointsForPlot


class SpatialStatistics(SpeedCalc):  # subclass, inherits from SpeedCalc
    """
    Subclass for GDAL-related spatial statistics
    """

    def __init__(self, formula=False, number_of_decimals=6):
        """
        Initializes subclass SpatialStatistics
        """
        super(SpeedCalc, self).__init__()
        self._df = "0." + str(number_of_decimals) + "f"  # Sets up print format string, e.g. 0.6f
        self._formula = formula
        self._numberOfDecimals = number_of_decimals

        # Initialize Instance Attributes that are used later
        self.rasterName = None
        self.raster_as_array = None
        self.gdalRasterData = None
        self.outputFilename = None
        self.columns = None
        self.rows = None
        self._w = None
        self._y = None
        self.lag_distance = None
        self.min_distance = None
        self.max_distance = None

    def read_raster_as_array(self, raster_name):
        """
        Reads an input raster into a Numpy array

        :param raster_name:
        :return:
        """

        self.rasterName = raster_name
        self.gdalRasterData = gdal.Open(self.rasterName, GA_ReadOnly)
        self.rows = self.gdalRasterData.RasterYSize
        self.columns = self.gdalRasterData.RasterXSize
        self.raster_as_array = self.gdalRasterData.ReadAsArray()
        # [self.columns, self.rows] = self.raster_as_array.shape

        return self.raster_as_array

    def save_raster_array_to_geotiff(self, raster_as_array, output_filename):
        """
        Saves raster as Numpy Array out to a GeoTiff file
        Helpful reference: http://blog.remotesensing.io/2013/03/using-gdal-with-python-basic-intro/

        @param raster_as_array: The raster as a Numpy array
        @param output_filename: The path of the file concatentated with its path as a string
        :return:
        """
        self.raster_as_array = raster_as_array
        self.outputFilename = output_filename
        _transformation = self.gdalRasterData.GetGeoTransform()
        _projection = self.gdalRasterData.GetProjection()
        _rasterBand = self.gdalRasterData.GetRasterBand(1)
        _noDataValue = _rasterBand.GetNoDataValue()
        _outfilePath = self.outputFilename

        # Create the file, using the information from the original file
        _outdriver = gdal.GetDriverByName("GTiff")
        _outdata = _outdriver.Create(str(_outfilePath), self.rows, self.columns, 1, GDT_Float32)

        # Write the array to the file, which is the original array in this example
        _outdata.GetRasterBand(1).WriteArray(self.raster_as_array)

        # Set a no data value if required
        if _noDataValue is not None:
            _outdata.GetRasterBand(1).SetNoDataValue(_noDataValue)

        # Georeference the image
        _outdata.SetGeoTransform(_transformation)

        # Write projection information
        _outdata.SetProjection(_projection)

    def calc_morans_i(self, raster_as_array, lag_distance=10):
        """
        Calculates the value of Moran's I at given lag distances using Distance Band Weights;
        Default ranges from 1 pixel to 10 pixels
        In this particular project, that translates to: 1 pixel (30 m) to 10 pixels (300 m)

        Reference: http://pysal.readthedocs.org/en/latest/users/tutorials/weights.html#distance-band-weights
        @param raster_as_array: the raster to use in the calculations as an array
        @param lag_distance: given lag distance
        @returns: an array of Moran's I values.
        """
        self.raster_as_array = raster_as_array
        self.lag_distance = lag_distance

        _flattened_raster_array = self.raster_as_array.ravel()
        _x, _y = numpy.indices((self.rows, self.columns))
        _x.shape = (self.rows * self.columns, 1)
        _y.shape = (self.rows * self.columns, 1)
        _horizontal_stack = numpy.hstack([_x, _y])

        _Morans_I = numpy.zeros(self.lag_distance)

        # Get weights based on distance (distance-band method) and calculation Moran's I
        for i in range(1, self.lag_distance + 1):
            _wthresh = pysal.threshold_binaryW_from_array(_horizontal_stack, i)  # distance-based weights
            _mi = pysal.Moran(_flattened_raster_array, _wthresh)  # calculate Moran's I for given distance
            _Morans_I[i-1] = _mi.I  # Value of individual result of Moran's I (_mi.I) saved into array

        return _Morans_I

    def get_lag_distance_for_plot(self, min_distance, max_distance):
        """

        :param min_distance:
        :param max_distance:
        :return:
        """
        self.min_distance = min_distance
        self.max_distance = max_distance
        return numpy.linspace(self.min_distance, self.max_distance, self.lag_distance)
