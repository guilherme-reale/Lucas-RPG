import pygame
import random

from lib.sprites import *
from lib.config import *
from lib.camera import CameraGroup

from lib.dialogue import *
import lib.gameData as gameData

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
                    if gameData.player_data['pos_x'] == 0 and gameData.player_data['pos_y'] == 0:
                        self.player_pos = (x,y)
                    else:
                        self.player_pos =(gameData.player_data['pos_x'],gameData.player_data['pos_y']) 
                if col == 'd':
                    DangerZone((x,y),[self.visible_sprites,self.danger_sprites])
                if col == 'n':
                    Npc("img/NPC_s/NPC-Test.png",(x,y),npc_text['npc1'],[self.visible_sprites,self.obstacle_sprites,self.npc_sprites])
                if col == 'm':
                    image = pygame.image.load("img/NPC_s/NPC Mulher TE Morena Vermelho.png").convert_alpha()
                    image_scaled = pygame.transform.scale(image,(64,64))
                    Npc(image_scaled,(x,y),npc_text['npc1'],[self.visible_sprites,self.obstacle_sprites,self.npc_sprites])
                if col == 'o':
                    image = pygame.image.load("img/NPC_s/NPC Mulher TE Morena Roxo.png").convert_alpha()
                    image_scaled = pygame.transform.scale(image,(64,64))
                    Npc(image_scaled,(x,y),npc_text['npc1'],[self.visible_sprites,self.obstacle_sprites,self.npc_sprites])
                if col == 'r':
                    image = pygame.image.load("img/NPC_s/NPC Mulher Morena.png").convert_alpha()
                    image_scaled = pygame.transform.scale(image,(64,64))
                    Npc(image_scaled,(x,y),npc_text['npc1'],[self.visible_sprites,self.obstacle_sprites,self.npc_sprites])
                if col == 'q':
                    image = pygame.image.load("img/NPC_s/NPC Mulher Loira.png").convert_alpha()
                    image_scaled = pygame.transform.scale(image,(64,64))
                    Npc(image_scaled,(x,y),npc_text['npc1'],[self.visible_sprites,self.obstacle_sprites,self.npc_sprites])
                
        self.player = Player(self.player_pos,[self.visible_sprites],self.obstacle_sprites,self.danger_sprites,self.npc_sprites)            
                
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


        
        
        