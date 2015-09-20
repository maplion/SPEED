#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 05: Calculating Vapor Pressure Deficit.

Computes values of VPD for a 24 hour period at a meteorological station in the Dry Creek Experimental Watershed

Note: methods (and their specific names) included in this module are here to meet the listed requirements

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import speedcalc

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_Pressure = speedcalc.Pressure(units="kPa")

# TODO: Compute values of VPD for a 24 hour period at a meteorological station in the Dry Creek Experimental Watershed by using a for loop and making the appropriate call to the getVPD function


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


print(getVPD(50, 65))
