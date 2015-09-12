#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 04: Saturation Vapor Pressure calculations from temperature

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import matplotlib.pyplot as plt
import speedcalc

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_Pressure = speedcalc.Pressure(numberOfDecimals=2)

vaporPressureList = []
temperatureList = []
temperature = -15.0
while temperature < 35.01:
    vaporPressure = sc_Pressure.saturationVaporPressure(temperature, resultPascal="kPa")
    print("T = {0} deg. C, esat = {1} kPa".format(temperature, vaporPressure))
    vaporPressureList.append(vaporPressure)
    temperatureList.append(temperature)
    temperature += 0.01
plt.plot(temperatureList, vaporPressureList)
plt.xlabel("Temperature [Celsius Degrees]")
plt.ylabel("Saturation vapor pressure (e*) [kPa]")
plt.show()
