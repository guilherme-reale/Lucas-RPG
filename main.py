import pygame 
import sys
import json

from level import Level
from battle import Battle
from sprites import *
from text import Text
from config import *
import player_data as pd


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("As Aventuras Ecológicas de Lucas")
        #tela principal
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        #definição da taxa de quadros
        self.clock = pygame.time.Clock()
        #fonte dos textos
        self.font = pygame.font.Font(MAIN_FONT,32)
        #Eventos definem o que será mostrado em cada momento do jogo
        self.event = 'TITLE SCREEN'
    
        game_icon = pygame.transform.scale2x(pygame.image.load("img/NPC-Test.png").convert_alpha())
        pygame.display.set_icon(game_icon)
        
        #carrega o save com as informações do jogador    
        try:
            with open('player-data.txt') as load_file:
                pd.player_data = json.load(load_file)
        except:
            #cria o save
            with open('player-data.txt','w') as store_file:
                json.dump(pd.player_data,store_file)
        
        #instância da fase
        self.level = Level()
        #instância da tela de batalhas
        self.battle_phase = Battle()
        
    def main_game(self):
        while True:
            for event in pygame.event.get():
                #opção de fechar janela
                if event.type == pygame.QUIT:
                    #salva o jogo
                    with open("player-data.txt",'w') as store_data:
                        json.dump(pd.player_data,store_data)
                        
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
        screen_image = pygame.image.load("img/TITLE-SCREEN.png").convert_alpha()
        screen_image = pygame.transform.scale(screen_image,(1280,720))
        self.screen.blit(screen_image,(0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.event = 'OVERWORLD'
    
    #Movimentação no cenário
    def overworld(self):
        self.screen.fill("#5D8AA8")
        self.battle_phase.event = ''
        self.level.run()
        if self.level.player.battle_time == True:
            self.event = 'BATTLE'
    
    #tela de batalhas        
    def battle(self):
        self.battle_phase.run()
        if self.battle_phase.event == "OVERWORLD":
            self.level.player.true_to_false()
            self.event = 'OVERWORLD'
        
        
game= Game()
game.main_game()