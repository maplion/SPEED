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

con_Time.secondToMinute(60)
con_Time.minuteToSecond(1)
con_Length.meterToMillimeter(10000)
con_Time.secondToHour(3600)
con_Time.secondToMinute(60)
con_Time.hourToMinute(1)
con_Time.hourToSecond(1)
con_Time.minuteToHour(60)
