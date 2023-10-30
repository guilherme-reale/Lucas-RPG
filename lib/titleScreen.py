import pygame,json

import lib.gameData as gameData
from lib.text import Text, Button
from lib.config import *


class TitleScreen:
    def __init__(self):
        self.new_game = Button("Novo Jogo",35,WIDTH//2,200,orientation='center')
        self.load_game = Button("Continuar Jogo",35,WIDTH//2,250,orientation='center')
        self.event = 'TITLE SCREEN'
    
    def make_title(self,screen,map):
        screen_image = pygame.image.load("img/Title Screen/TITLE-SCREEN.png").convert_alpha()
        screen_image = pygame.transform.scale(screen_image,(1280,720))
        screen.blit(screen_image,(0,0))
        main_text = Text("As Aventuras Ecológicas de Lucas",43,WIDTH//2,100,orientation='center')
        main_text.draw(screen)
        
        self.render(screen)
        self.transition(map)
        
    def render(self,screen):
        self.new_game.draw(screen)
        self.new_game.update()
        self.load_game.draw(screen)
        self.load_game.update()
    
    def transition(self,map):
        mousePos = pygame.mouse.get_pos()
        mouseKeys = pygame.mouse.get_pressed()
        new_game_collision = self.new_game.rect.collidepoint(mousePos)
        load_game_collision = self.load_game.rect.collidepoint(mousePos)
        
        if new_game_collision and mouseKeys[0]:
            gameData.player_data = gameData.player_data_default
            map.create_map(gameData.player_data['map'])
            self.event = "OVERWORLD"
        elif load_game_collision and mouseKeys[0]:
            try:
                with open('player-data.txt') as load_file:
                    gameData.player_data = json.load(load_file)
            except:
                #cria o save
                with open('player-data.txt','w') as store_file:
                    json.dump(gameData.player_data,store_file)
            map.create_map(gameData.player_data['map'])
            self.event = "OVERWORLD"