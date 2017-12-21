# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:46:14 2017

@author: cisdi
"""

from otherfunctions import * 

units_path = 'C:/Users/cisdi/Desktop/单位.xlsx'
units = get_units(units_path) #从字典中获取单位


output_path = 'C:/Users/cisdi/Desktop/output/'

f2 = open(output_path + 'units.data' , 'w')

units.pop(0)

for i in units:
    f2.write(i)
    f2.write(',')

f2.close()
    




