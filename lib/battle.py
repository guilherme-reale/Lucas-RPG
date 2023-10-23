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
        self.enemy = Enemy(self.text_display)
        self.show_hp = Text(f"HP: {self.player.stats['hp']}",16,WIDTH//2,500)
        self.show_lvl = Text(f"LVL {self.player.stats['lvl']}",16,WIDTH//2 + 100,500)
        self.event = ''
        self.counter = 0
        self.done = False
        
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
                pass
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
                self.state = BattleState.PLAYER
        elif self.state == BattleState.RUN:
            self.player.update_stats()
            self.player = PlayerBattle(self.buttons,self.text_display)
            self.counter+=0.1
            if self.counter >= 12:
                self.counter = 0
                self.text_display.lines.clear()
                self.enemy = Enemy(self.text_display)
                self.event = 'OVERWORLD'
        elif self.state == BattleState.VICTORY:
            if not self.done:
                self.text_display.add_message("Lucas derrotou o inimigo!")
                self.player.winnings(self.enemy)
                self.player.level_up()
                self.player.update_stats()
                self.player = PlayerBattle(self.buttons,self.text_display)
                self.done = True
            self.counter+=0.1
            if self.counter>=12:
                self.done = False
                self.counter = 0
                self.text_display.lines.clear()
                self.enemy = Enemy(self.text_display)
                self.event = 'OVERWORLD'
            
            
                
        

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
        self.render(screen)
        self.handle_events(events)
        self.update()

            

        
        