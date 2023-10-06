import pygame
from config import *
import math
import random
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
    def __init__(self,pos,group,obstacle_sprites,danger_sprites):
        super().__init__(group)
        
        self.player_spritesheet = Spritesheet("img/Char_one/Char_4_sides.png")
        
        self.image = self.player_spritesheet.get_sprite(0,0,16,PLAYER_HEIGHT,4)
        self.rect = self.image.get_rect(center = pos)
        
        self.direction = pygame.math.Vector2()
        self.orientation = 'DOWN'
        
        self.loop = 0
        
        self.obstacle_sprites = obstacle_sprites
        self.danger_sprites = danger_sprites
        
        self.steps = 0
        
        self.gameAlert = False
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.steps+=STEP
            self.orientation = 'UP'
            self.animation("img/Char_one/Walk/Char_walk_up.png")
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.steps+=STEP
            self.orientation = 'DOWN'
            self.animation("img/Char_one/Walk/Char_walk_down.png")
        else:
            self.direction.y = 0
        
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.steps+=STEP
            self.orientation = 'LEFT'
            self.animation("img/Char_one/Walk/Char_walk_left.png")
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.steps+=STEP
            self.orientation = 'RIGHT'
            self.animation("img/Char_one/Walk/Char_walk_right.png")
        else:
            self.direction.x = 0 
        
        if self.direction.x == 0 and self.direction.y == 0:
            if self.orientation == 'DOWN':
                self.image = self.player_spritesheet.get_sprite(0,0,16,PLAYER_HEIGHT,4)
            elif self.orientation == 'RIGHT':
                self.image = self.player_spritesheet.get_sprite(16,0,16,PLAYER_HEIGHT,4)
            elif self.orientation == 'UP':
                self.image = self.player_spritesheet.get_sprite(32,0,16,PLAYER_HEIGHT,4)
            elif self.orientation == 'LEFT':
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
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.x +=self.direction.x * SPEED
        self.collision('horizontal')
        self.rect.y +=self.direction.y * SPEED
        self.collision('vertical')
        
        self.danger_collision()
        
    def danger_collision(self):
        for sprite in self.danger_sprites:
            if self.rect.colliderect(sprite.rect):
                if self.steps>100 and random.randint(0,100) < 5:
                    self.gameAlert = True
                    self.steps = 0
    
    def collision (self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                
    def update(self):
        self.input()
        self.moviment()        

class Npc(pygame.sprite.Sprite):
    def __init__(self,image,pos,text,player,group,item=None):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.text = text
        self.item = item
        self.player = player
        self.text_active = False
        self.screen = pygame.display.get_surface()
        
    def input(self):
        mousepress = pygame.mouse.get_pressed()
        if self.player.rect.colliderect(self.rect) and mousepress[0]:
            self.text_active = not self.text_active
            
    def display_text(self):
        if self.text_active:
            text_surface = pygame.Surface((WIDTH,HEIGHT/6))
            text_rect = text_surface.get_rect(topleft = (0,0))
            if text_rect.colliderect(self.rect):
                text_rect.bottomright = (WIDTH,HEIGHT)
            pygame.draw.rect(text_surface,WHITE,text_rect,5)
            
            test_obj = Text(self.text,23,0,0)
            test_obj.draw(text_surface)
            self.screen.blit(text_surface,text_rect)            
    
    def update(self):
        self.input()
        self.display_text()
        

class Tile(pygame.sprite.Sprite):
    def __init__(self,image,pos,group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(center=pos)       
    
class DangerZone(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=pos)
        

        
        