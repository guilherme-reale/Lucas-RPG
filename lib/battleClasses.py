import pygame,random

import lib.gameData as gameData
from lib.text import Text
from lib.config import *

class Enemy:
    def __init__(self,text_display):
        self.image = pygame.image.load(PLASTICO).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ENEMY_POSITION
        self.stats = gameData.plastico_stats
        self.hp = self.stats['hp_max']
        self.text = text_display
        self.last_clicked_time = 0
        self.coin = random.randint(gameData.plastico_stats['coin'],gameData.plastico_stats['coin']+20)
        self.exp = gameData.plastico_stats['exp']
    
    def enemy_attack(self,player):
        damage = max(self.stats['atk'] - player.stats['def'],1)        
        self.text.add_message(f"Inimigo ataca: {damage} de dano!")
        player.stats['hp'] = max(player.stats['hp']-damage,0)
    
    def lower_defense(self,player):
        rd = random.randint(1,3)
        self.text.add_message(f"Inimigo emite um som estranho! Menos {rd} de defesa!")
        player.stats['def'] = max(player.stats['def']-rd,0)
        
    
        
class PlayerBattle:
    def __init__(self,buttons,display_text):
        self.buttons = buttons
        self.stats = {
            'hp': gameData.player_data['hp'],
            'atk': gameData.player_data['atk'],
            'def': gameData.player_data['def'],
            'exp': gameData.player_data['exp'],
            'lvl': gameData.player_data['lvl'],
            'coin': gameData.player_data['coin'],
            'potion': gameData.player_data['potion'] 
        }
        self.last_clicked_time = 0
        self.run = False
        self.win = False
        self.text = display_text
    
    def player_attack(self,enemy):
        damage = max(self.stats['atk'] - enemy.stats['def'],1)
        self.text.add_message(f"Lucas ataca:{damage} de dano!")
        enemy.hp = max(enemy.hp-damage,0)
        print(enemy.hp)
        
    def player_potion(self):
        if self.stats['potion'] > 0:
            self.text.add_message(f"Lucas usou uma poção e recuperou {POTION_HP} de HP!")
            self.stats['hp'] = min(self.stats['hp']+POTION_HP,gameData.player_data['hp_max'])
            self.stats['potion'] -=1
            return 1
        else:
            self.text.add_message("Lucas não tem poção!")
            return 0
        
    def player_run(self):    
             
        if random.randint(0,2) == 0:
            self.text.add_message("Lucas conseguiu correr do inimigo!")
            return 4
        
    
        else:
            self.text.add_message("Lucas não conseguiu correr do inimigo!")
            return 1
    def winnings(self,enemy):
        self.text.add_message(f"Lucas ganhou {enemy.exp} de experiência e {enemy.coin} tokens!")
        self.stats['coin'] += enemy.coin
        self.stats['exp']+= enemy.exp
        
    def level_up(self): pass
    def update_stats(self):
        gameData.player_data['hp'] = self.stats['hp']
        gameData.player_data['exp'] = self.stats['exp']
        gameData.player_data['lvl'] = self.stats['lvl']
        gameData.player_data['coin'] = self.stats['coin']
        gameData.player_data['potion'] = self.stats['potion']