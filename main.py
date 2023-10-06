import pygame 
import sys
from level import Level
from battle import Battle
from sprites import *
from text import Text
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
        self.event = 'TITLE SCREEN'
        
        #instância da fase
        self.level = Level()
        self.battle = Battle()
        
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
        pass
        
        
game= Game()
game.main_game()