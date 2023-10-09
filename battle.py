import pygame
from config import *
from text import *

class Battle:
    def __init__(self):
        self.screen = pygame.display.get_surface()
    
    def draw(self):
        
        self.screen.fill(BLACK)
        
        main_rect = pygame.Surface((WIDTH - 100,HEIGHT//3))
        main_rect_rect = main_rect.get_rect(center = (WIDTH/2,HEIGHT/2))
        pygame.draw.rect(self.screen,"White",main_rect_rect,10)
        
        hp = Text("HP: 35",16,WIDTH//2,500)
        hp.draw(self.screen)
        
        lvl = Text("LVL 1",16,WIDTH//2 + 100,500)
        lvl.draw(self.screen)
        
        rect_size = main_rect_rect.right - main_rect_rect.left
        rect_font = 42
        
        atacar = Buttons("ATACAR",rect_font,main_rect_rect.left,HEIGHT-100)
        atacar.draw(self.screen)
        atacar.update()
        
        magia = Text("MAGIA",rect_font,main_rect_rect.left+rect_size/4,HEIGHT-100)
        magia.draw(self.screen)
        
        itens = Text("ITENS",rect_font,main_rect_rect.left+rect_size/2,HEIGHT-100)
        itens.draw(self.screen)
        
        correr = Text("CORRER",rect_font,main_rect_rect.left+rect_size*3/4,HEIGHT-100)
        correr.draw(self.screen)
        
    
    
    def run(self): 
        self.draw()
        