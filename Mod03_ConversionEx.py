# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:29:58 2015

@author: Ryan Dammrose aka MapLion
"""

import speedcalc

sc_Time = speedcalc.Time()
sc_ET = speedcalc.ET()
sc_Length = speedcalc.Length()

ET_mf = 3.0e-5
ET_ef = 30
ET_ef_2 = 100

ET_mf_result = sc_ET.massFluxToWaterEvaporated(ET_mf)
ET_ef_result = sc_ET.energyFluxToWaterEvaporated(ET_ef)
ET_ef_2_result = sc_ET.energyFluxToWaterEvaporated(ET_ef_2)

print("For ET = {0} kg/(m^2*s), I get ET = {1} mm/day".format(ET_mf, ET_mf_result))
print("For ET = {0} W/m^2, I get ET = {1} mm/day".format(ET_ef, ET_ef_result))
print("For ET = {0} W/m^2, I get ET = {1} mm/day".format(ET_ef_2, ET_ef_2_result))
