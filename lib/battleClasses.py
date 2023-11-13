"""
Módulos:
- pygame: Biblioteca para desenvolvimento de jogos em Python.
- random: Módulo para geração de números aleatórios.

Classes:
- Enemy: Classe que representa um inimigo durante uma batalha.
- PlayerBattle: Classe que representa o personagem do jogador durante uma batalha.

Métodos e Atributos da Classe Enemy:
- __init__(self, text_display, boss=False): Inicializa a classe Enemy. Determina características do inimigo com base no mapa atual.
- enemy_attack(self, player): Realiza um ataque ao jogador, calculando o dano com base em estatísticas.
- lower_defense(self, player): Reduz a defesa do jogador e exibe uma mensagem.
- draw(self, screen): Desenha a imagem do inimigo na tela.

Atributos da Classe Enemy:
- boss: Indica se o inimigo é um chefe.
- stats: Dicionário contendo as estatísticas do inimigo.
- image, rect: Imagem e retângulo que representam visualmente o inimigo.
- hp: Pontos de vida do inimigo.
- text: Instância da classe Text para exibição de mensagens.
- coin, exp: Recompensas concedidas ao jogador ao derrotar o inimigo.

Métodos e Atributos da Classe PlayerBattle:
- __init__(self, buttons, display_text): Inicializa a classe PlayerBattle. Recebe instâncias dos botões e do display de texto.
- player_attack(self, enemy): Realiza um ataque ao inimigo, calculando o dano com base nas estatísticas do jogador.
- player_magic(self, enemy): Realiza um ataque mágico ao inimigo, consumindo moedas e causando dano.
- player_potion(self): Usa uma poção para recuperar pontos de vida do jogador.
- player_run(self): Tenta fugir do inimigo com uma chance de sucesso de 1/3.
- winnings(self, enemy): Concede recompensas ao jogador ao derrotar o inimigo.
- level_up(self): Aumenta o nível do jogador com base na experiência acumulada.
- update_stats(self): Atualiza as estatísticas do jogador no módulo gameData.

Atributos da Classe PlayerBattle:
- buttons: Lista de instâncias da classe Button representando os botões de ação.
- stats: Dicionário contendo as estatísticas do jogador.
- text: Instância da classe Text para exibição de mensagens.

Módulos e Variáveis Adicionais:
- import lib.gameData as gameData: Importa o módulo gameData.
- from lib.text import Text: Importa a classe Text do módulo lib.text.
- from lib.config import *: Importa variáveis de configuração globais.

"""

import pygame,random

import lib.gameData as gameData
from lib.text import Text
from lib.config import *

class Enemy:
    def __init__(self,text_display,boss=False):
        self.boss = False
        if gameData.player_data['map'] == MAP_PLASTICO:
            img = PLASTICO
            self.stats = gameData.plastico_stats
        elif gameData.player_data['map'] == MAP_PAPELAO:
            img = PAPELAO
            self.stats = gameData.papelao_stats
        elif gameData.player_data['map'] == MAP_METAL:
            img = METAL
            self.stats = gameData.metal_stats
        elif gameData.player_data['boss'] == 1:
            img = TOXICO
            self.stats = gameData.boss_stats
            self.boss = True
        else:
            img = TOXICO
            self.stats = gameData.toxico_stats
        self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(),(128,128))
        self.rect = self.image.get_rect()
        self.rect.center = ENEMY_POSITION   
        self.hp = self.stats['hp_max']
        self.text = text_display
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
        if random.randint(0,1) == 1:
            self.text.add_message("Lucas ganhou uma poção!")
            self.stats['potion']+=1
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