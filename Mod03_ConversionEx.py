# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:29:58 2015

@author: Ryan Dammrose aka MapLion
"""

import speedcalc

sc_Time = speedcalc.Time(printFormula="true")
sc_ET = speedcalc.ET(printFormula="true")
sc_Length = speedcalc.Length(printFormula="true")

sc_ET.massFluxToWaterEvaporated(3.0e-5)
sc_ET.energyFluxToWaterEvaporated(120)
