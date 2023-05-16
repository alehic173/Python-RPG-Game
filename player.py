# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:09:33 2023

@author: alexa
"""

import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/alexa/OneDrive/Desktop/Python-RPG-Game/graphics/player/left_idle/idle_left.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites =obstacle_sprites
        
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
        
        # Normalize angled movement so that it is not faster than horiz/vert
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
         # Adjust speed and set up collision   
        self.hitbox.x += self.direction.x*speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y*speed 
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
        
            
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # if moving right, prevent player from overlapping
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                   # if moving left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # if moving down
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                   # if moving up
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
        
    def update(self):
        self.key_input()
        self.move(self.speed)