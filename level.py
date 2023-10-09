import pygame
from sprites import *
from config import *
from camera import CameraGroup
import random
from game_dialogue import *
import player_data as pd

class Level:
    def __init__(self):
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.danger_sprites = pygame.sprite.Group()
        self.npc_sprites = pygame.sprite.Group()
        
        self.display_surface = pygame.display.get_surface()
        
        self.create_map()
        
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                # tile_sheet = Spritesheet("img/overworld.png")
                # tile_image = tile_sheet.get_sprite(48,48,32,32,2)
                # Tile(tile_image,(x,y),[self.visible_sprites])
                
                if col == 'x':
                    Tile("img/rock.png",(x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    if pd.player_data['pos_x'] == 0 and pd.player_data['pos_y'] == 0:
                        self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.danger_sprites,self.npc_sprites)
                    else:
                        self.player = Player((pd.player_data['pos_x'],pd.player_data['pos_y']),[self.visible_sprites],self.obstacle_sprites,self.danger_sprites,self.npc_sprites)
                if col == 'd':
                    DangerZone((x,y),[self.visible_sprites,self.danger_sprites])
                if col == 'n':
                    Npc("img/NPC-Test.png",(x,y),npc_text['npc1'],[self.visible_sprites,self.obstacle_sprites,self.npc_sprites])
                
                    
                
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


        
        
        