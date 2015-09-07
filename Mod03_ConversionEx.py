# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:29:58 2015

@author: Ryan Dammrose aka MapLion
"""

import convert

con = convert.Convert()
con_Time = convert.Time(printFormula="true")
con_ET = convert.ET(printFormula="true")
con_Length = convert.Length(printFormula="true")

con_ET.massFluxToWaterEvaporated(3.0e-5)
con_ET.energyFluxToWaterEvaporated(120)
