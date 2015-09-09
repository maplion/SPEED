# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 22:40:00 2015

@author: Ryan Dammrose aka MapLion
"""

import convert

con_Pressure = convert.Pressure(printFormula="true")
con_Pressure.saturationVaporPressure(20, resultPascal="kpa")