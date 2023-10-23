import pygame
from pytmx.util_pygame import load_pygame

from lib.sprites import *
from lib.config import *
from lib.camera import CameraGroup

from lib.dialogue import *
import lib.gameData as gameData

class Map:
    def __init__(self):
        
        
        self.display_surface = pygame.display.get_surface()
        
        
        
        self.recycle_sprites = Spritesheet(RECYCLE_SPRITES)   
        
        self.entrance = self.entranceS = self.entranceW = self.entranceE = self.entranceN = None
        self.previous_map = ''
        
        self.create_map(gameData.player_data['map'])
        
    def create_map(self,map):
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.danger_sprites = pygame.sprite.Group()
        self.npc_sprites = pygame.sprite.Group()
        
        
        self.tmx_data = load_pygame(map)
        self.create_visible_layer()
        self.create_object_layer()
        
        if gameData.player_data['pos_x'] == None and gameData.player_data['pos_y'] == None:
            self.player_pos = (160,160)
        else:
            self.player_pos =(gameData.player_data['pos_x'],gameData.player_data['pos_y']) 
        
        self.player = Player(self.player_pos,[self.visible_sprites],self.obstacle_sprites,self.danger_sprites,self.npc_sprites)
                   
    def create_visible_layer(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'):
                for x,y,surf in layer.tiles():
                    pos = (x*TILESIZE,y*TILESIZE)
                    surf = pygame.transform.scale(surf,(TILESIZE,TILESIZE))
                    
                    Tile(surf,pos,[self.visible_sprites])
    
    def create_object_layer(self):
        for obj in self.tmx_data.objects:
            pos = (obj.x*TILESIZE/16,obj.y*TILESIZE/16)
            
            if obj.name=='ground':
                Tile(pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos,[self.visible_sprites,self.obstacle_sprites],origin='topleft')
            elif obj.name == 'recycle1':
                Tile(self.recycle_sprites.get_sprite(0,0,18,64,0.9),pos,[self.visible_sprites])
            elif obj.name == 'recycle2':
                Tile(self.recycle_sprites.get_sprite(19,0,39,64,0.9),pos,[self.visible_sprites])
            elif obj.name == 'recycle3':
                Tile(self.recycle_sprites.get_sprite(59,0,37,64,0.9),pos,[self.visible_sprites])
            elif obj.name == 'entrance':
               self.entrance = Tile(pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos,[self.visible_sprites],origin='topleft')
            elif obj.name == 'danger':
                Tile(pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos,[self.visible_sprites,self.danger_sprites],origin='topleft')
            elif obj.name == 'entranceS':
                self.entranceS = Tile(pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos,[self.visible_sprites],origin='topleft')
                
            else:
                
                #surf = pygame.transform.scale(obj.image,(TILESIZE,TILESIZE))
                Tile(obj.image,pos, [self.visible_sprites])
            

    def level_transition(self):
        if gameData.player_data['map'] == MAP_CENTRAL:
            pass
        else:
            if self.player.rect.x < 0 or self.player.rect.x > HEIGHT or self.player.rect.y < 0 or self.player.rect.y > WIDTH:
                self.previous_map = gameData.player_data['map']
                gameData.player_data['map'] = MAP_CENTRAL
                self.create_map(MAP_CENTRAL)
                self.player.hitbox.center = (WIDTH//2,HEIGHT)
            
            
               
                        
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.level_transition()


        
        
        