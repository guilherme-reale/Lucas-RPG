import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacle_sprites,danger_sprites):
        super().__init__(group)
        
        self.image = pygame.transform.scale2x(pygame.image.load("img/characters/char_down.png").convert_alpha())
        self.rect = self.image.get_rect(center = pos)
        
        self.direction = pygame.math.Vector2()
        
        self.obstacle_sprites = obstacle_sprites
        self.danger_sprites = danger_sprites
        
        self.steps = 0
        
        self.gameAlert = False
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.steps+=STEP
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.steps+=STEP
        else:
            self.direction.y = 0
        
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.steps+=STEP
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.steps+=STEP
        else:
            self.direction.x = 0
    
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
                    print("test")
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

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load("img/rock.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)       
    
class DangerZone(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=pos)
        
        