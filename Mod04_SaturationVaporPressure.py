# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 22:40:00 2015

@author: Ryan Dammrose aka MapLion
"""

import speedcalc
import matplotlib.pyplot as plt

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
