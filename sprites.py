import pygame
import math
import random
from config import *
import player_data as pd
from text import Text

class Spritesheet:
    def __init__(self,file):
        self.sheet = pygame.image.load(file).convert_alpha()
    
    def get_sprite(self,x,y,width,height,scale=1):
             
        sprite = pygame.Surface((width,height))
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite = pygame.transform.scale(sprite,(width*scale,height*scale))
        sprite.set_colorkey(BLACK)
        
        return sprite
        

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacle_sprites,danger_sprites,npc_sprites):
        super().__init__(group)
        
        self.player_spritesheet = Spritesheet(PLAYER_IDLE)
        
        self.image = self.player_spritesheet.get_sprite(0,0,16,PLAYER_HEIGHT,4)
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(0,-20)
        
        self.direction = pygame.math.Vector2()
        self.orientation = 'DOWN'

        
        self.loop = 0
        
        self.obstacle_sprites = obstacle_sprites
        self.danger_sprites = danger_sprites
        self.npc_sprites = npc_sprites
        
        self.steps = 0
        
        self.battle_time = False
        
        self.pause = False
        
        self.surface = pygame.display.get_surface()
        
        self.dialog_open = False  
        self.text_index = 0  
        
        self.last_clicked_time = 0
        
        
        
    def movement_input(self):
        keys = pygame.key.get_pressed()        
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.direction.x = 0
            self.orientation = 'UP'
            self.animation("img/Char_one/Walk/Char_walk_up.png")
        elif keys[pygame.K_a]:
            self.direction.y = 0
            self.direction.x = -1
            self.orientation = 'LEFT'
            self.animation("img/Char_one/Walk/Char_walk_left.png") 
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.direction.x = 0
            self.orientation = 'DOWN'
            self.animation("img/Char_one/Walk/Char_walk_down.png")
        elif keys[pygame.K_d]:
            self.direction.y = 0
            self.direction.x = 1
            self.orientation = 'RIGHT'
            self.animation("img/Char_one/Walk/Char_walk_right.png")
        else:
            self.direction.x = 0
            self.direction.y = 0 
            self.idle(self.orientation)
        
        
    def idle(self,orientation):
        if orientation == 'DOWN':
            self.image = self.player_spritesheet.get_sprite(0,0,16,PLAYER_HEIGHT,4)
        elif orientation == 'RIGHT':
            self.image = self.player_spritesheet.get_sprite(16,0,16,PLAYER_HEIGHT,4)
        elif orientation == 'UP':
            self.image = self.player_spritesheet.get_sprite(32,0,16,PLAYER_HEIGHT,4)
        elif orientation == 'LEFT':
            self.image = self.player_spritesheet.get_sprite(48,0,16,PLAYER_HEIGHT,4)
        
    
    def animation(self,file):
        player_movement = []
        player_movement_sheet = Spritesheet(file)
        for i in range(6):
            player_movement.append(player_movement_sheet.get_sprite(i*16,0,16,PLAYER_HEIGHT,4))
        self.image = player_movement[int(self.loop)]
        self.loop+=0.1
        self.loop%=len(player_movement)
        

    def moviment(self):
        dx = self.direction.x * SPEED
        dy = self.direction.y * SPEED
        self.steps+= math.dist((self.hitbox.x+dx,self.hitbox.y+dy),(self.hitbox.x,self.hitbox.y))/4     
        self.hitbox.x += dx
        self.collision('horizontal')
        self.hitbox.y += dy
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
        pd.player_data['pos_x'] = self.hitbox.x
        pd.player_data['pos_y'] = self.hitbox.y
                
        self.danger_collision()
        
    def danger_collision(self):
        for sprite in self.danger_sprites:
            if self.hitbox.colliderect(sprite.rect):
                if self.steps>100 and random.randint(0,100) < 5:
                    self.battle_time = True
                    self.steps = 0
    
    def collision (self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.rect.bottom
    
    def npc_collision(self):
        mouse = pygame.mouse.get_pressed()
        for sprite in self.npc_sprites:
            if self.hitbox.colliderect(sprite.hitbox):
                current_time = pygame.time.get_ticks()
                if mouse[0] and current_time -self.last_clicked_time > 1000:
                    self.last_clicked_time = current_time
                    self.current_npc = sprite 
                    self.dialog_open = True  
                    self.pause = True
                 
    def npc_text(self):
        if self.dialog_open and self.pause:
            npc_text = Text(self.current_npc.text[self.text_index], 22, 0, 0)
            npc_text.draw_box((WIDTH, HEIGHT/6), (0, 0), self.surface,True,2)
            current_time = pygame.time.get_ticks()
            if pygame.mouse.get_pressed()[0] and current_time - self.last_clicked_time > 500:
                self.last_clicked_time = current_time
                self.text_index += 1
                if self.text_index >= len(self.current_npc.text):
                    self.text_index = 0  
                    self.dialog_open = self.pause = False

       
    def update(self):
        if self.pause == False:
            self.movement_input()
            self.moviment()
            self.npc_collision()  
        self.npc_text()     

class Npc(pygame.sprite.Sprite):
    def __init__(self,image,pos,text,group,item=None):
        super().__init__(group)
        
        self.text = text
        
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(5,5)
            
        
class Tile(pygame.sprite.Sprite):
    def __init__(self,image,pos,group):
        super().__init__(group)
        
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
            
        self.rect = self.image.get_rect(center=pos)       
    
class DangerZone(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=pos)
        

        
        