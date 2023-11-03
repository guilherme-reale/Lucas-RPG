import pygame
from pytmx.util_pygame import load_pygame

from lib.sprites import *
from lib.config import *
from lib.camera import CameraGroup

from lib.npcs import MakeNPC
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
            self.player_pos = (420,420)
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
            
            elif obj.name == 'recycle4':
                Tile(self.recycle_sprites.get_sprite(97,0,53,64,0.9),pos,[self.visible_sprites])
                
            elif obj.name == 'recycle5':
                Tile(self.recycle_sprites.get_sprite(150,0,54,64,0.9),pos,[self.visible_sprites])
            
            elif obj.name == 'recycle6':
                Tile(self.recycle_sprites.get_sprite(205,0,36,64,0.9),pos,[self.visible_sprites])
                
            elif obj.name == 'recycle10':
                Tile(self.recycle_sprites.get_sprite(304,0,24,64,0.9),pos,[self.visible_sprites])
                
            elif obj.name == 'recycle11':
                Tile(self.recycle_sprites.get_sprite(330,0,21,64,0.9),pos,[self.visible_sprites])
                
            elif obj.name == 'recycle12':
                Tile(self.recycle_sprites.get_sprite(352,0,19,64,0.9),pos,[self.visible_sprites])
                
            elif obj.name == 'recycle14':
                Tile(self.recycle_sprites.get_sprite(402,0,61,64,0.9),pos,[self.visible_sprites])
                
            elif obj.name == 'recycle16':
                Tile(self.recycle_sprites.get_sprite(495,0,18,64,0.9),pos,[self.visible_sprites])
                
            elif obj.name == 'danger':
                Tile(pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos,[self.visible_sprites,self.danger_sprites],origin='topleft')
                
            elif obj.name == 'save':
                Npc(image=pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos = pos,
                    text=["Retornar à casa após uma longa jornada é sempre recompensador.","O seu progresso foi salvo."],
                    group=[self.visible_sprites,self.obstacle_sprites,self.npc_sprites],is_save_point=True)
                
            elif obj.name == 'potion':
                potion_text = ["A água limpa mantém o corpo jovem e cura doenças.", "Proteja esta fonte evitando o descarte inadequado de materiais tóxicos.","HP recuperado."]
                 
                Npc(image=pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos = pos,
                    text=potion_text,
                    group=[self.visible_sprites,self.obstacle_sprites,self.npc_sprites],is_potion=True)
            
            elif obj.name == 'boss':
                boss_text = ["Nós fomos criados graças ao descaso dos humanos com o meio ambiente.",
                             "Todos nós poderíamos ter um destino correto.",
                             "Poderíamos estar nas casas, nas escolas, servindo aos humanos.",
                             "Mas vocês preferiram nos descartar.",
                             "Estamos cansados disso!",
                             "Venha e me enfrente, se tiver coragem!"
                             ]
                Npc(image=pygame.Surface((obj.width*TILESIZE/16,obj.height*TILESIZE/16),pygame.SRCALPHA),pos = pos,
                    text=boss_text,
                    group=[self.visible_sprites,self.obstacle_sprites,self.npc_sprites],is_boss=True)
            
                
            else:
                
                #surf = pygame.transform.scale(obj.image,(TILESIZE,TILESIZE))
                Tile(obj.image,pos, [self.visible_sprites])
            

    def level_transition(self):
        pos_x = self.player.hitbox.x
        pos_y = self.player.hitbox.y
        
        if gameData.player_data['map'] == MAP_CENTRAL:
            if pos_x < 40*4 and pos_y in range(140*4,180*4):
                self.load_map(MAP_METAL,(305*4,144*4))
            elif pos_x > 275*4 and pos_y in range(140*4,180*4):
                self.load_map(MAP_PAPELAO,(11*4,161*4))
            elif pos_x in range(140*4,180*4) and pos_y < 40*4:
                self.load_map(MAP_TOXICO,(271*4,316*4))
            elif pos_x in range (140*4,180*4) and pos_y > 275*4:
                self.load_map(MAP_PLASTICO,(168*4,11*4))
        elif gameData.player_data['map'] == MAP_PAPELAO:
            if pos_x < 0 and self.player.direction.x == -1:
                self.load_map(MAP_CENTRAL,(420,420))
        elif gameData.player_data['map'] == MAP_PLASTICO:
            if pos_y < 0 and self.player.direction.y == -1:
                self.load_map(MAP_CENTRAL,(420,420))
        elif gameData.player_data['map'] == MAP_METAL:
            if pos_x > 1280 and self.player.direction.x == 1:
                self.load_map(MAP_CENTRAL,(420,420))  
        elif gameData.player_data['map'] == MAP_TOXICO:
            if pos_y > 1280 and self.player.direction.y == 1:
                self.load_map(MAP_CENTRAL,(420,420))
            
    def load_map(self,map,pos):
        gameData.player_data['map'] = map
        self.create_map(map)
        self.player.hitbox.center = pos
                        
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.level_transition()


        
        
        