# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:29:58 2015

@author: Ryan Dammrose aka MapLion
"""

import convert

con = convert.Convert()
con_Time = convert.Time(printFormula="true")
con_ET = convert.ET()
con_Length = convert.Length()

con_Time.secondToMinute(60)
con_Time.minuteToSecond(1)