# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:29:58 2015

@author: Ryan Dammrose aka MapLion
"""

import speedcalc

con_Time = speedcalc.Time(printFormula="true")
con_ET = speedcalc.ET(printFormula="true")
con_Length = speedcalc.Length(printFormula="true")

con_ET.massFluxToWaterEvaporated(3.0e-5)
con_ET.energyFluxToWaterEvaporated(120)
