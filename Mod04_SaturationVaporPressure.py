# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 22:40:00 2015

@author: Ryan Dammrose aka MapLion
"""

import speedcalc

sc_Pressure = speedcalc.Pressure(printFormula="true")
sc_Pressure.saturationVaporPressure(10, resultPascal="kPa")