import pygame
from config import *
from text import *

class Battle:
    def __init__(self):
        pass
    
    def draw(self):
        self.screen = pygame.display.get_surface()
        self.screen.fill(BLACK)
        
        main_rect = pygame.Surface((WIDTH - 100,HEIGHT//3))
        main_rect_rect = main_rect.get_rect(center = (WIDTH/2,HEIGHT/2))
        pygame.draw.rect(self.screen,"White",main_rect_rect,10)
        
        hp = self.font.render('HP: 35',False,"White")
        hp_rect = hp.get_rect(midtop = (WIDTH/2,500))
        self.screen.blit(hp,hp_rect)
        
        lvl = self.font.render('LVL 1',False,"White")
        lvl_rect = lvl.get_rect(midtop = (WIDTH/2 + 100,500))
        self.screen.blit(lvl,lvl_rect)
        
        atacar = Text("ATACAR",72,main_rect_rect.left,HEIGHT-100)
        atacar.draw(self.screen)
        
        magia = Text("MAGIA",72,(main_rect_rect.right - main_rect_rect.left)/4,HEIGHT-100)
        magia.draw(self.screen)
        
        itens = Text("ITENS",72,(main_rect_rect.right - main_rect_rect.left)/2,HEIGHT-100)
        itens.draw(self.screen)
        
        correr = Text("CORRER",72,(main_rect_rect.right - main_rect_rect.left)*0.9,HEIGHT-100)
        correr.draw(self.screen)
        
    
    
    def run(self):
        pass