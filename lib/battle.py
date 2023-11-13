"""
Módulos:
- pygame: Biblioteca para desenvolvimento de jogos em Python.
- random: Módulo para geração de números aleatórios.

Classes:
- BattleState: Enumeração para definir estados da batalha.
- Battle: Classe responsável pela lógica e renderização do sistema de batalha.

Métodos e Atributos da Classe BattleState:
- PLAYER, ENEMY, GAME_OVER, VICTORY, RUN: Constantes para representar os estados da batalha.

Métodos e Atributos da Classe Battle:
- __init__(): Inicializa a classe Battle. Define os elementos gráficos da interface de batalha e instâncias de classes relacionadas.
- handle_events(events): Manipula eventos do mouse durante a batalha.
- update(): Atualiza o estado da batalha com base nas ações dos jogadores e inimigos.
- render(screen): Renderiza a interface gráfica da batalha na tela.
- run(screen, events): Executa o loop principal da batalha, renderizando e atualizando continuamente.

Atributos da Classe Battle:
- state: Estado atual da batalha (PLAYER, ENEMY, GAME_OVER, VICTORY, RUN).
- main_rect, main_rect_rect: Superfície gráfica e retângulo correspondente para a interface principal da batalha.
- rect_size, rect_font: Tamanho do retângulo e fonte utilizados na interface.
- atacar, magia, pocao, correr: Instâncias da classe Button representando opções de ação do jogador.
- buttons: Lista contendo as instâncias de botões de ação.
- text_display: Instância da classe TextDisplay para exibição de mensagens na tela.
- turn_count: Contador para controlar a contagem de turnos.
- processing, previous_time: Flags para controle de eventos e tempo antigo de clique.
- player: Instância da classe PlayerBattle representando o jogador na batalha.
- show_hp, show_lvl: Instâncias da classe Text para exibir informações de HP e nível do jogador.
- event, counter, done, load_enemy: Variáveis para controle de eventos, contagem e estado de carga do inimigo.

Métodos e Atributos Adicionais:
- handle_events(): Manipula os eventos do mouse durante a batalha, acionando as ações dos botões.
- update(): Atualiza o estado da batalha com base nas ações dos jogadores e inimigos.
- render(): Renderiza a interface gráfica da batalha na tela.
- run(): Executa o loop principal da batalha, renderizando e atualizando continuamente.
"""

import pygame, random

from lib.battleClasses import PlayerBattle,Enemy
from lib.text import *
from lib.config import *



class BattleState:
    PLAYER = 0
    ENEMY = 1
    GAME_OVER = 2
    VICTORY = 3
    RUN = 4

class Battle:
    def __init__(self):
        self.state = BattleState.PLAYER
        self.main_rect = pygame.Surface((WIDTH - 100,HEIGHT//3))
        self.main_rect_rect = self.main_rect.get_rect(center = (WIDTH/2,HEIGHT/2))
        self.rect_size = self.main_rect_rect.right - self.main_rect_rect.left
        self.rect_font = 42
        self.atacar = Button("ATACAR",self.rect_font,self.main_rect_rect.left,HEIGHT-100)
        self.magia = Button("MAGIA",self.rect_font,self.main_rect_rect.left+self.rect_size/4,HEIGHT-100)
        self.pocao = Button("POÇÃO",self.rect_font,self.main_rect_rect.left+self.rect_size/2,HEIGHT-100)
        self.correr = Button("CORRER",self.rect_font,self.main_rect_rect.left+self.rect_size*3/4,HEIGHT-100)
        self.buttons = [self.atacar,self.magia,self.pocao,self.correr]
        self.text_display = TextDisplay(32, 100, HEIGHT//3, 5, WIDTH - 20, HEIGHT - 20)
        self.turn_count = 0
        self.processing = False 
        self.previous_time = 0
        self.player = PlayerBattle(self.buttons,self.text_display)
        
        self.show_hp = Text(f"HP: {self.player.stats['hp']}",16,WIDTH//2,500)
        self.show_lvl = Text(f"LVL {self.player.stats['lvl']}",16,WIDTH//2 + 100,500)
        self.event = ''
        self.counter = 0
        self.done = False
        self.load_enemy = False
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.processing:
                if self.state == BattleState.PLAYER:
                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos):
                            button.on_click()

    def update(self):
        if self.state == BattleState.PLAYER:
            if self.buttons[0].is_mouse_pressed:
                self.player.player_attack(self.enemy)
                self.buttons[0].release_click()
                self.turn_count+=1
            elif self.buttons[1].is_mouse_pressed:
                self.state = self.player.player_magic(self.enemy)
                self.buttons[1].release_click()
            elif self.buttons[2].is_mouse_pressed:
                self.state = self.player.player_potion()
                self.buttons[2].release_click()
            elif self.buttons[3].is_mouse_pressed:
                self.buttons[3].release_click()
                self.state = self.player.player_run()
            
            
            if self.turn_count >= 1:  # Simulando fim do turno do jogador
                self.turn_count = 0
                if self.enemy.hp > 0:
                    self.state = BattleState.ENEMY
                else:
                    self.state = BattleState.VICTORY

        elif self.state == BattleState.ENEMY:
            if random.randint(0,2) > 0:
                self.enemy.enemy_attack(self.player)
            else:
                self.enemy.lower_defense(self.player)
            self.turn_count+=1
            
            if self.turn_count >= 1:  # Simulando fim do turno do inimigo
                self.turn_count = 0
                if self.player.stats['hp'] > 0:
                    
                    self.state = BattleState.PLAYER
                
                else:
                    self.state = BattleState.GAME_OVER
                
        elif self.state == BattleState.RUN:
            self.player.update_stats()
            
            self.counter+=0.1
            if self.counter >= 12:
                self.counter = 0
                self.text_display.lines.clear()
                self.load_enemy = False
                self.event = 'OVERWORLD'
                
        elif self.state == BattleState.VICTORY:
            if not self.done:
                self.text_display.add_message("Lucas derrotou o inimigo!")
                self.player.winnings(self.enemy)
                self.player.level_up()
                self.player.update_stats()
                
                self.done = True
            self.counter+=0.1
            if self.counter>=12:
                self.done = False
                self.counter = 0
                self.text_display.lines.clear()
                
                if self.enemy.boss:
                    self.event = 'ENDING'
                else:
                    self.load_enemy = False
                    self.event = 'OVERWORLD'
        
        elif self.state == BattleState.GAME_OVER:
            if not self.done:
                self.text_display.add_message("Lucas foi derrotado!")
                self.done = True
            
            self.counter+=0.1
            if self.counter >= 12:
                self.done = False
                self.counter = 0
                self.text_display.lines.clear()
                self.load_enemy = False
                
                self.event = 'GAME OVER'   
            
                
        

    def render(self, screen):
        screen.fill(BLACK)
        pygame.draw.rect(screen,WHITE,self.main_rect_rect,10)
        for button in self.buttons:
            button.draw(screen)
            button.update()
        self.text_display.draw(screen)
        self.show_hp.draw(screen)
        self.show_hp.new_text(f"HP: {self.player.stats['hp']}")
        self.show_lvl.draw(screen)
        
        # Outros elementos da interface gráfica

    def run(self,screen,events):
        if not self.load_enemy:
            self.player = PlayerBattle(self.buttons,self.text_display)
            self.enemy = Enemy(self.text_display)
            self.load_enemy = True
        
        self.render(screen)
        self.enemy.draw(screen)
        self.handle_events(events)
        self.update()

            

        
        