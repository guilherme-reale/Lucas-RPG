"""
As Aventuras Ecológicas de Lucas - Jogo em Python utilizando a biblioteca Pygame

Módulos:
- gameData: Módulo para armazenar dados do jogo.
- map: Módulo para gerenciar o mapa do jogo.
- battle: Módulo para controlar as batalhas no jogo.
- text: Módulo para manipular texto na interface do jogo.
- titleScreen: Módulo para gerenciar a tela inicial do jogo.
- config: Módulo contendo configurações globais.

Classe:
- Game: Classe principal que controla o fluxo do jogo.

Métodos da Classe Game:
- __init__(): Inicializa o jogo, configura a janela, carrega recursos e instância objetos.
- main_game(): Loop principal do jogo que gerencia os eventos e chama os métodos adequados.
- title_screen(): Método para exibir a tela inicial do jogo.
- overworld(): Método para controlar a fase de exploração do mapa.
- introduction(): Método para exibir a introdução do jogo (vazio no momento).
- battle(): Método para controlar as batalhas no jogo.
- game_over(): Método para exibir a tela de Game Over.
- ending(): Método para exibir a tela de finalização do jogo.
- battle_transition(): Método para realizar a transição visual entre a exploração e as batalhas.

Atributos da Classe Game:
- screen: Janela principal do jogo.
- clock: Relógio para controlar a taxa de quadros.
- font: Fonte para renderizar texto.
- event: Estado atual do jogo ('TITLE SCREEN', 'INTRODUCTION', 'OVERWORLD', 'BATTLE', 'GAME OVER', 'ENDING').
- map: Instância do mapa do jogo.
- battle_phase: Instância do gerenciador de batalhas.
- title_screen_instance: Instância da tela inicial.
- animation_counter: Contador para animações visuais.
- time_counter: Contador de tempo para eventos específicos.
- play_music: Flag para controlar a reprodução de música no jogo.
"""

import pygame,sys,json

import lib.gameData as gameData
from lib.map import Map
from lib.battle import Battle
from lib.text import Text,Button
from lib.titleScreen import TitleScreen
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
        self.event = "TITLE SCREEN"
    
        game_icon = pygame.transform.scale2x(pygame.image.load("img/NPC_s/NPC-Test.png").convert_alpha())
        pygame.display.set_icon(game_icon)
        
        
        
        
        #instância da fase
        #self.map = map()
        self.map = Map()
        #instância da tela de batalhas
        self.battle_phase = Battle()
        
        self.title_screen_instance = TitleScreen()
        
        self.animation_counter = 0
        self.time_counter = 0 
        
        self.play_music = True      
        
    def main_game(self):
        while True:
           
            gameData.player_data['time'] = str(pygame.time.get_ticks()//(1000*3600))+":"+ str(pygame.time.get_ticks()//(1000*60)%60)
            events = pygame.event.get()
            for event in events:
                #opção de fechar janela
                if event.type == pygame.QUIT:
                    #fecha o jogo  
                    pygame.quit()
                    sys.exit()
                    
            #definição dos eventos
            if self.event == 'TITLE SCREEN':
                self.title_screen()
            elif self.event == 'INTRODUCTION':
                self.introduction()
            elif self.event == 'OVERWORLD':
                self.overworld()
            elif self.event == 'BATTLE':
                self.battle(events)
            elif self.event == 'GAME OVER':
                self.game_over()
            elif self.event == 'ENDING':
                self.ending()
                
                
            pygame.display.update()
            self.clock.tick(FPS)
    
    #tela inicial
    def title_screen(self):
        self.title_screen_instance.event = 'TITLE SCREEN'
        self.title_screen_instance.make_title(self.screen,self.map)
        self.event = self.title_screen_instance.event
    
    #Movimentação no cenário
    def overworld(self):
        if self.play_music:
            pygame.mixer.music.load("music/music_overworld.ogg")
            pygame.mixer.music.play(-1)
            self.play_music = False
        
        self.screen.fill("#5D8AA8")
        self.battle_phase.event = ''
        self.battle_phase.state = 0
        self.map.run()
        if self.map.player.battle_time == True:
            pygame.mixer.music.fadeout(1000)
            self.map.player.pause_player()
            self.map.player.exclamation_emote()
            self.time_counter+=0.1
            if self.time_counter >=6: 
                if self.battle_transition():
                    self.time_counter = 0
                    self.play_music = True
                    self.event = "BATTLE"
                    
    def introduction(self):
        pass
    #tela de batalhas        
    def battle(self,events):
        if self.play_music:
            pygame.mixer.music.load("music/music_battle.ogg")
            pygame.mixer.music.play(-1)
            self.play_music = False
        self.battle_phase.run(self.screen,events)
        if self.battle_phase.event == "OVERWORLD":
            self.map.player.true_to_false()
            self.map.player.unpause_player()
            pygame.mixer.music.fadeout(100)
            self.play_music = True
            self.event = 'OVERWORLD'
        elif self.battle_phase.event == "GAME OVER":
            pygame.mixer.music.fadeout(100)
            self.play_music = True
            self.event = "GAME OVER"
        elif self.battle_phase.event == 'ENDING':
            pygame.mixer.music.fadeout(100)
            self.play_music = True
            self.event = "ENDING"
            
            
    def game_over(self):
        self.screen.fill(BLACK)
        image = pygame.image.load("img/Title Screen/GAME-OVER.png").convert_alpha()
        self.screen.blit(image,(0,0))
        if pygame.mouse.get_pressed()[0]:
            self.event = "TITLE SCREEN"
    
    def ending(self):
        if self.play_music:
            pygame.mixer.music.load("music/music_ending.mp3")
            pygame.mixer.music.play(-1)
            self.play_music = False
        self.screen.fill(BLACK)
        text1 = Text("Parabéns, você derrotou os monstros!",50,WIDTH//2,100,orientation='center')
        text2 = Text("Agora, para que não apareçam mais, temos que manter a cidade limpa.",30,WIDTH//2,200,orientation='center')
        text3 = Text("Vamos reciclar!",30,WIDTH//2,300,orientation='center')
        
        for text in text1, text2, text3:
            text.draw(self.screen)
    
    def battle_transition(self):
        # Usar pygame.SRCALPHA para suporte a canal alfa
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  
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
        
        
