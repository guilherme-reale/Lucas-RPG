import pygame,random

import lib.gameData as gameData
from lib.text import Text
from lib.config import *

class Enemy:
    def __init__(self,text_display,boss=False):
        if gameData.player_data['map'] == MAP_PLASTICO:
            img = PLASTICO
            self.stats = gameData.plastico_stats
        elif gameData.player_data['map'] == MAP_PAPELAO:
            img = PAPELAO
            self.stats = gameData.papelao_stats
        elif gameData.player_data['map'] == MAP_METAL:
            img = METAL
            self.stats = gameData.metal_stats
        else:
            img = TOXICO
            self.stats = gameData.toxico_stats
        self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(),(128,128))
        self.rect = self.image.get_rect()
        self.rect.center = ENEMY_POSITION   
        self.hp = self.stats['hp_max']
        self.text = text_display
        self.last_clicked_time = 0
        self.coin = random.randint(gameData.plastico_stats['coin'],gameData.plastico_stats['coin']+20)
        self.exp = gameData.plastico_stats['exp']
    
    def enemy_attack(self,player):
        damage = max(self.stats['atk'] - player.stats['def']+random.randint(0,3),1)        
        self.text.add_message(f"Inimigo ataca: {damage} de dano!")
        player.stats['hp'] = max(player.stats['hp']-damage,0)
    
    def lower_defense(self,player):
        rd = random.randint(1,3)
        self.text.add_message(f"Inimigo emite um som estranho! Menos {rd} de defesa!")
        player.stats['def'] = max(player.stats['def']-rd,0)
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
class PlayerBattle:
    def __init__(self,buttons,display_text):
        self.buttons = buttons
        self.stats = {
            'hp': gameData.player_data['hp'],
            'hp_max': gameData.player_data['hp_max'],
            'atk': gameData.player_data['atk'],
            'atk_max': gameData.player_data['atk'],
            'def': gameData.player_data['def'],
            'def_max': gameData.player_data['def'],
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
        critical = 1 if random.randint(0,10) > 3 else 2
        damage = max(self.stats['atk'] - enemy.stats['def']*critical,1)
        self.text.add_message(f"Lucas ataca:{damage} de dano!")
        enemy.hp = max(enemy.hp-damage,0)
    
    
    def player_magic(self,enemy):
        damage = 30 + self.stats['atk'] - enemy.stats['def']
        if self.stats['coin'] >= 20:
            self.text.add_message(f"Lucas usou magia: {damage} de dano!")
            enemy.hp = max(enemy.hp - damage,0)
            self.stats['coin'] -= 20
            return 1
        else:
            self.text.add_message("Lucas não tem tokens o suficiente!")
            return 0
        
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
        self.stats['lvl'] = max(self.stats['exp']//(100+10*self.stats['lvl']),self.stats['lvl'])
        
    def level_up(self): 
        if self.stats['lvl'] > gameData.player_data['lvl']:
            self.text.add_message("Lucas subiu de nível!")
            new_hp = random.randint(0,10)//3
            new_atk = random.randint(0,8)//3
            new_def = random.randint(0,8)//3
            self.text.add_message(f"+{new_hp} de hp! + {new_atk} de ataque! +{new_def} de defesa!")
            self.stats['hp_max']+=new_hp
            self.stats['atk_max']+=new_atk
            self.stats['def_max']+=new_def
        
        
    def update_stats(self):
        gameData.player_data['hp'] = self.stats['hp']
        gameData.player_data['hp_max'] = self.stats['hp_max']
        gameData.player_data['atk'] = self.stats['atk_max']
        gameData.player_data['def'] = self.stats['def_max']
        gameData.player_data['exp'] = self.stats['exp']
        gameData.player_data['lvl'] = self.stats['lvl']
        gameData.player_data['coin'] = self.stats['coin']
        gameData.player_data['potion'] = self.stats['potion']