import pygame
from config import *
from text import *

class Battle:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.event = ""
        self.main_rect = pygame.Surface((WIDTH - 100,HEIGHT//3))
        self.main_rect_rect = self.main_rect.get_rect(center = (WIDTH/2,HEIGHT/2))
        self.rect_size = self.main_rect_rect.right - self.main_rect_rect.left
        self.rect_font = 42
        self.hp = Text("HP: 35",16,WIDTH//2,500)
        self.lvl = Text("LVL 1",16,WIDTH//2 + 100,500)
        self.atacar = Buttons("ATACAR",self.rect_font,self.main_rect_rect.left,HEIGHT-100)
        self.magia = Buttons("MAGIA",self.rect_font,self.main_rect_rect.left+self.rect_size/4,HEIGHT-100)
    def draw(self):
        
        self.screen.fill(BLACK)
        
        
        pygame.draw.rect(self.screen,"White",self.main_rect_rect,10)
        
        
        self.hp.draw(self.screen)
        
        
        self.lvl.draw(self.screen)
        
        self.atacar.draw(self.screen)

        #magia = Text("MAGIA",rect_font,main_rect_rect.left+rect_size/4,HEIGHT-100)
        #magia.draw(self.screen)
        
        #itens = Text("ITENS",rect_font,main_rect_rect.left+rect_size/2,HEIGHT-100)
        #itens.draw(self.screen)
        
        #correr = Text("CORRER",rect_font,main_rect_rect.left+rect_size*3/4,HEIGHT-100)
        #correr.draw(self.screen)
        
    def input(self):
        self.atacar.hover()
        if self.atacar.clicked() == True:
            self.event = "OVERWORLD"
        
        
    
    def run(self): 
        self.draw()
        self.input()
        
        