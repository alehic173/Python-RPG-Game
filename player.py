# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:09:33 2023

@author: alexa
"""

import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/alexa/OneDrive/Desktop/Python-RPG-Game/graphics/player/left_idle/idle_left.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        
    def key_input(self):
        keys = pygame.key.get_pressed()
        
        # "UP" or "DOWN" key inputs, modify direction.y
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1  
        else:
            self.direction.y = 0
        
        # "RIGHT" or "LEFT" key inputs, modify direction.x
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1  
        else:
            self.direction.x = 0
            
    def move(self, speed):
        self.rect.center += self.direction * speed
            
    
    def update(self):
        self.key_input()
        self.move(self.speed)