# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:31:12 2023

@author: alexa
"""
from csv import reader
# Import the Tiled layout with areas that the character cannot walk through
def import_csv_layout(path):
    
   terrain_map = [] 
   with open(path) as level_map:
       layout = reader(level_map,delimiter= ',')
       for row in layout:
           terrain_map.append(list(row))
       return terrain_map
           



