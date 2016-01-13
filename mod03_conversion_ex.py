#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 03: Unit Conversions for mass flux and energy flux

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import speedcalc

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_Time = speedcalc.Time()
sc_ET = speedcalc.ET()
sc_Length = speedcalc.Length()

ET_mf = 3.0e-5
ET_ef = 30
ET_ef_2 = 100

ET_mf_result = sc_ET.mass_flux_to_water_evaporated(ET_mf)
ET_ef_result = sc_ET.energy_flux_to_water_evaporated(ET_ef)
ET_ef_2_result = sc_ET.energy_flux_to_water_evaporated(ET_ef_2)

print("For ET = {0} kg/(m^2*s), I get ET = {1} mm/day".format(ET_mf, ET_mf_result))
print("For ET = {0} W/m^2, I get ET = {1} mm/day".format(ET_ef, ET_ef_result))
print("For ET = {0} W/m^2, I get ET = {1} mm/day".format(ET_ef_2, ET_ef_2_result))
