# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:21:41 2023

@author: alexa
"""
import pygame

class Level:
    def __init__(self):
        
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
    def run(self):
        
        # update and draw the game
        pass