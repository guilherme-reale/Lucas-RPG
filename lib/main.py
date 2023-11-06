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
        self.event = 'TITLE SCREEN'
    
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
            
            
    def game_over(self):
        self.screen.fill(BLACK)
        image = pygame.image.load("img/Title Screen/GAME-OVER.png").convert_alpha()
        self.screen.blit(image,(0,0))
        if pygame.mouse.get_pressed()[0]:
            self.event = "TITLE SCREEN"
    
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
        
        
