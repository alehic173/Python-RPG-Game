# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:21:41 2023

@author: alexa
"""
import pygame
from settings import *
from tile import Tile
from player import Player
from debug import *
from support import *

class Level:
    def __init__(self):
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.create_map()
    def create_map(self):
        layouts = {
                'boundary': import_csv_layout('C:/Users/alexa/OneDrive/Desktop/Python-RPG-Game/map/map_FloorBlocks.csv')
                }
        # iterate through each item in layouts dictionary
        # find x and y positions 
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != '-1':
                        x = column_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites], 'invisible',)
            #     if column == 'x':
            #         Tile((x,y), [self.visible_sprites,self.obstacle_sprites])
            #     if column == 'p':
            #         self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)   
        self.player = Player((2000,1430), [self.visible_sprites], self.obstacle_sprites)  
        
    def run(self):
        
        
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
        # update and draw the game
        pass
    
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
       
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
        # getting the coordinates for the middle of the screen
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        # at the beginning, set camera to 100,200
        self.camera = pygame.math.Vector2(100,200)
        # self.camera = pygame.math.Vector2(0,0)
        self.floor_surface = pygame.image.load('C:/Users/alexa/OneDrive/Desktop/Python-RPG-Game/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

        
    def custom_draw(self, player):
        
        # adjust camera to center the player
        self.camera.x = player.rect.centerx - self.half_width
        self.camera.y = player.rect.centery - self.half_height
        
        # placing floor before everything else
        floor_offset_pos = self.floor_rect.topleft - self.camera
        self.display_surface.blit(self.floor_surface, floor_offset_pos)
        
        # display all sprites including player
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # key is y position of each sprite
            camera_pos = sprite.rect.topleft - self.camera
            self.display_surface.blit(sprite.image, camera_pos)
            
            
            
            
            
            
            
            
            