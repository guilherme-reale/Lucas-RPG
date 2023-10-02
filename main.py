import pygame 
import sys
from level import *
from sprites import *
from config import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("As Aventuras Ecológicas de Lucas")
        #tela principal
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        #definição da taxa de quadros
        self.clock = pygame.time.Clock()
        #fonte dos textos
        self.font = pygame.font.Font("font/Pixeltype.ttf",32)
        #Eventos definem o que será mostrado em cada momento do jogo
        self.event = 'BATTLE'
        
        #instância da fase
        self.level = Level()
        
    def main_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            #definição dos eventos
            if self.event == 'TITLE SCREEN':
                self.title_screen()
            elif self.event == 'OVERWORLD':
                self.overworld()
            elif self.event == 'BATTLE':
                self.battle()
            pygame.display.update()
            self.clock.tick(FPS)
    
    #tela inicial
    def title_screen(self):
        self.screen.fill("#23261f")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.event = 'OVERWORLD'
    
    
    #Movimentação no cenário
    def overworld(self):
        self.screen.fill("#5D8AA8")
        self.level.run()
        if self.level.player.gameAlert == True:
            self.event = 'BATTLE'
            
    def battle(self):
        self.screen.fill((0,0,0))
        
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
        
            


game= Game()
game.main_game()