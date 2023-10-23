import pygame,math,random

import lib.gameData as gameData
from lib.text import *
from lib.config import *

class Spritesheet:
    def __init__(self,file):
        self.sheet = pygame.image.load(file).convert_alpha()
    
    def get_sprite(self,x,y,width,height,scale=1):
             
        sprite = pygame.Surface((width,height),pygame.SRCALPHA)
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite = pygame.transform.scale(sprite,(width*scale,height*scale))
        #sprite.set_colorkey(BLACK)
        
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
        self.menu_open = False
        self.text_index = 0  
        
        self.last_clicked_time = 0
        self.snip = 1
        
        self.emotes = Spritesheet("img/emotes/emotes.png")
        
        
    def movement_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.add_movement(-1, 0, 'UP')
        elif keys[pygame.K_a]:
            self.add_movement(0, -1, 'LEFT')
        elif keys[pygame.K_s]:
            self.add_movement(1, 0, 'DOWN')
        elif keys[pygame.K_d]:
            self.add_movement(0, 1, 'RIGHT')
        else:
            self.direction.x = 0
            self.direction.y = 0 
            self.idle(self.orientation)

    # TODO Rename this here and in `movement_input`
    def add_movement(self, arg0, arg1, arg2):
        self.direction.y = arg0
        self.direction.x = arg1
        self.orientation = arg2
        self.animation(arg2)
        
        
    def idle(self,orientation):
        if orientation == 'DOWN':
            self.image = self.player_spritesheet.get_sprite(0,0,16,PLAYER_HEIGHT,4)
        elif orientation == 'RIGHT':
            self.image = self.player_spritesheet.get_sprite(16,0,16,PLAYER_HEIGHT,4)
        elif orientation == 'UP':
            self.image = self.player_spritesheet.get_sprite(32,0,16,PLAYER_HEIGHT,4)
        elif orientation == 'LEFT':
            self.image = self.player_spritesheet.get_sprite(48,0,16,PLAYER_HEIGHT,4)
        
    
    def animation(self,orientation):
        player_movement = []
        player_movement_sheet = Spritesheet(PLAYER_MOVING)
        
        if orientation == 'UP':
            height = 32
        elif orientation == 'DOWN':
            height = 0
        elif orientation == "LEFT":
            height = 16
        elif orientation == 'RIGHT':
            height = 48
            
        for i in range(4):
            player_movement.append(player_movement_sheet.get_sprite(i*16,height,16,PLAYER_HEIGHT,4))
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
        
        gameData.player_data['pos_x'] = self.hitbox.x
        gameData.player_data['pos_y'] = self.hitbox.y
                
        self.danger_collision()
        
    def danger_collision(self):
        for sprite in self.danger_sprites:
            if self.hitbox.colliderect(sprite.rect):
                if self.steps>100 and random.randint(0,200) < 1:
                    self.battle_time = True
                    self.steps = 0
                
                
    def true_to_false(self): self.battle_time = False
    def pause_player(self): self.pause = True
    def unpause_player(self): self.pause = False
    
    def menu(self):
        mousekeys = pygame.mouse.get_pressed()
        current_time = pygame.time.get_ticks()
        if mousekeys[2] and current_time - self.last_clicked_time > 1000:
            self.last_clicked_time = current_time
            self.pause = not self.pause
            self.menu_open = not self.menu_open
    
    def menu_screen(self):
        menu_surface = pygame.Surface((WIDTH*0.22,HEIGHT*0.8))
        menu_surface.fill(BLACK)
        menu_rect = menu_surface.get_rect()
        menu_rect.center = (WIDTH*0.75,HEIGHT*0.5)
        menu_text = [Text(f"HP: {gameData.player_data['hp']}/{gameData.player_data['hp_max']}",32,20,20),
                    Text(f"ATAQUE: {gameData.player_data['atk']}",32,20,80),
                    Text(f"DEFESA: {gameData.player_data['def']}",32,20,140),
                    Text(f"POÇÃO: {gameData.player_data['potion']}",32,20,300),
                    Text(f"EXP: {gameData.player_data['atk']}",32,20,360),
                    Text(f"TOKENS: {gameData.player_data['atk']}",32,20,420),
                    ]
        for text in menu_text:
            text.draw(menu_surface)
        self.surface.blit(menu_surface,menu_rect)
        pygame.draw.rect(self.surface,WHITE,menu_rect,5)
        
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
            #npc_text = Text(self.current_npc.text[self.text_index], 22, 0, 0)
            #npc_text.draw_box((WIDTH, HEIGHT/6), (0, 0), self.surface,True,2)
            npc_text = ScrollingText(self.current_npc.text[self.text_index], 22, 0, 0,self.snip)
            npc_text.draw_box((WIDTH, HEIGHT/6), (0, 0), self.surface,True,2)
            self.snip+=npc_text.speed
            current_time = pygame.time.get_ticks()
            if pygame.mouse.get_pressed()[0] and current_time - self.last_clicked_time > 500:
                self.last_clicked_time = current_time
                self.text_index += 1
                self.snip = 1
                if self.text_index >= len(self.current_npc.text):
                    self.text_index = 0  
                    self.dialog_open = self.pause = False

    def exclamation_emote(self):
        ex_emote = self.emotes.get_sprite(66,42,10,14,2)
        #ex_emote = pygame.image.load("img/emotes/exclamation mark.png").convert_alpha()
        ex_rect = ex_emote.get_rect()
        ex_rect.center = (WIDTH/2,HEIGHT/2)
        self.surface.blit(ex_emote,ex_rect)  
    def update(self):
        if self.pause == False:
            self.movement_input()
            self.moviment()
            self.npc_collision()  
        self.npc_text()
        self.menu() 
        if self.menu_open:
            self.menu_screen()    

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
    def __init__(self,image,pos,group,origin="center"):
        super().__init__(group)
        
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
            
        self.rect = self.image.get_rect()
        if origin =='center':
            self.rect.center = pos
        elif origin =='topleft':
            self.rect.topleft = pos
    
class DangerZone(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=pos)
        

        
        