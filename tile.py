# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:49:29 2023

@author: alexa
"""

import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/alexa/OneDrive/Desktop/Python-RPG-Game/graphics/objects/08.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        