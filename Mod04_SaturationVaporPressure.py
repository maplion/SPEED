# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 22:40:00 2015

@author: Ryan Dammrose aka MapLion
"""

import speedcalc
import matplotlib.pyplot as plt

sc_Pressure = speedcalc.Pressure()

vaporPressureList = []
temperatureList = []
temperature = -15.0
while temperature < 35.01:
    vaporPressure = sc_Pressure.saturationVaporPressure(temperature, resultPascal="kPa")
    print("T = {0} deg. C, esat = {1} kPa".format(temperature, round(vaporPressure, 2)))
    vaporPressureList.append(round(vaporPressure, 2))
    temperatureList.append(round(temperature, 2))
    temperature += 0.01
plt.plot(temperatureList, vaporPressureList)
plt.xlabel("Temperature [Celsius Degrees]")
plt.ylabel("Saturation vapor pressure (e*) [kPa]")
plt.show()