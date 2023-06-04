# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:31:12 2023

@author: alexa
"""
from csv import reader
from os import walk
import pygame
# Import the Tiled layout with areas that the character cannot walk through
def import_csv_layout(path):
    
   terrain_map = [] 
   with open(path) as level_map:
       layout = reader(level_map,delimiter= ',')
       for row in layout:
           terrain_map.append(list(row))
       return terrain_map
          
   
def import_folder(path):
    surface_list =[]
    for _,__,data in walk(path):
        for img in data:
            full_path = path + '/'+img
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)

    return surface_list


