import pygame 
import sys
import json

import lib.gameData as gameData
from lib.level import Level
from lib.battle import Battle
from lib.text import Text
from lib.config import *



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
    
        game_icon = pygame.transform.scale2x(pygame.image.load("img/NPC_s/NPC-Test.png").convert_alpha())
        pygame.display.set_icon(game_icon)
        
        #carrega o save com as informações do jogador    
        try:
            with open('player-data.txt') as load_file:
                gameData.player_data = json.load(load_file)
        except:
            #cria o save
            with open('player-data.txt','w') as store_file:
                json.dump(gameData.player_data,store_file)
        
        #instância da fase
        self.level = Level()
        #instância da tela de batalhas
        self.battle_phase = Battle()
        
        self.animation_counter = 0
        self.time_counter = 0
       
        
    def main_game(self):
        while True:
            events = pygame.event.get()
            for event in events:
                #opção de fechar janela
                if event.type == pygame.QUIT:
                    #salva o jogo
                    with open("player-data.txt",'w') as store_data:
                        json.dump(gameData.player_data,store_data)
                        
                    pygame.quit()
                    sys.exit()
                    
            #definição dos eventos
            if self.event == 'TITLE SCREEN':
                self.title_screen()
            elif self.event == 'INTRODUCTION':
                self.overworld()
            elif self.event == 'OVERWORLD':
                self.overworld()
            elif self.event == 'BATTLE':
                self.battle(events)
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
        self.battle_phase.state = 0
        self.level.run()
        if self.level.player.battle_time == True:
            self.level.player.pause_player()
            self.level.player.exclamation_emote()
            self.time_counter+=0.1
            if self.time_counter >=6: 
                if self.battle_transition():
                    self.time_counter = 0
                    self.event = "BATTLE"
                    
    def introduction(self):
        pass
    #tela de batalhas        
    def battle(self,events):
        self.battle_phase.run(self.screen,events)
        if self.battle_phase.event == "OVERWORLD":
            self.level.player.true_to_false()
            self.level.player.unpause_player()
            self.event = 'OVERWORLD'
    
    def battle_transition(self):
        # Usar pygame.SRCALPHA para suporte a canal alfa
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  
        # alpha = 0

        # while alpha < 255:
        #     # Preencha a superfície com uma cor preta e uma transparência baseada em 'alpha'
        #     surface.fill((0, 0, 0, alpha))
        #     self.screen.blit(surface, (0, 0))
        #     # Atualiza a tela a cada quadro
        #     pygame.display.flip()
        #     # Atraso para controlar a velocidade de escurecimento  
        #     pygame.time.delay(10)
        #     # Ajuste a velocidade como desejado  
        #     alpha += 2  

        # # Quando o escurecimento estiver completo, retorne True
        # return True

        
        self.battle_phase.render(surface)
        rect = surface.get_rect()
        rect.topright = (0+self.animation_counter,0)
        self.screen.blit(surface,rect)
        self.animation_counter+=15
        if rect.topright[0] >= WIDTH:
            self.animation_counter = 0
            return True
        else:
            return False
        
        
game= Game()
game.main_game()