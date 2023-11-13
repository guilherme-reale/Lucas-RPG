"""
Módulos:
- pygame: Biblioteca para desenvolvimento de jogos em Python.

Classes:
- Text: Classe que representa um bloco de texto na tela.
- Button: Subclasse de Text que representa um botão clicável.
- ScrollingText: Subclasse de Text que exibe um texto com rolagem.
- TextDisplay: Classe que gerencia e exibe um conjunto de mensagens na tela.

Métodos e Atributos da Classe Text:
- __init__(self, text, font_size, x, y, font=MAIN_FONT, orientation='topleft'): Inicializa a classe Text.
- draw_box(self, boxSize, boxPos, surface, drawBorder=False, borderWidth=1): Desenha um bloco de texto com caixa ao redor.
- new_text(self, new_text): Atualiza o texto exibido.
- draw(self, surface): Desenha o texto na superfície especificada.

Atributos da Classe Text:
- font: Fonte usada para renderizar o texto.
- text: Conteúdo do texto.
- font_size, x, y: Tamanho da fonte e posições x e y do texto.
- display_surface: Superfície de exibição do pygame.
- orientation: Orientação do texto (topleft ou center).
- color: Cor do texto (branco por padrão).
- image, rect: Superfície e retângulo do texto renderizado.

Métodos e Atributos da Classe Button (Subclasse de Text):
- __init__(self, text, font_size, x, y, font=MAIN_FONT, orientation='topleft'): Inicializa a classe Button.
- hover(self): Altera a cor do texto quando o mouse está sobre o botão.
- on_click(self): Ativa o estado de clique do botão.
- release_click(self): Desativa o estado de clique do botão.
- update(self): Atualiza o botão para resposta visual durante a interação.

Atributos Adicionais da Classe Button:
- last_clicked_time: Tempo da última vez que o botão foi clicado.
- is_mouse_pressed: Estado de pressionamento do botão.

Métodos e Atributos da Classe ScrollingText (Subclasse de Text):
- __init__(self, text, font_size, x, y, snip, font=MAIN_FONT): Inicializa a classe ScrollingText.
- draw_box(self, boxSize, boxPos, surface, drawBorder=False, borderWidth=1): Desenha um bloco de texto com rolagem em uma caixa.
- draw_scroll(self, surface): Atualiza o texto com rolagem, exibindo uma parte definida pelo parâmetro snip.

Atributos Adicionais da Classe ScrollingText:
- current_text: Texto atualmente visível após a rolagem.
- speed: Velocidade de rolagem.
- snip: Tamanho do texto a ser exibido.

Métodos e Atributos da Classe TextDisplay:
- __init__(self, font_size, x, y, max_lines, width, height, font=MAIN_FONT): Inicializa a classe TextDisplay.
- add_message(self, message): Adiciona uma mensagem à lista de mensagens, mantendo um número máximo definido por max_lines.
- draw(self, screen): Desenha as mensagens na tela.
- clear(self): Limpa a lista de mensagens.

Atributos da Classe TextDisplay:
- font: Fonte usada para renderizar as mensagens.
- x, y: Posições x e y do bloco de mensagens.
- max_lines: Número máximo de linhas de mensagem que o bloco pode conter.
- width, height: Largura e altura máximas do bloco de mensagens.
- lines: Lista de mensagens exibidas.

Módulos e Variáveis Adicionais:
- from lib.config import *: Importa variáveis de configuração globais.

"""

import pygame
from lib.config import *

class Text:
    def __init__(self,text, font_size, x, y,font=MAIN_FONT,orientation='topleft'):
        self.font = font
        self.text = text
        self.font_size = font_size
        self.x = x
        self.y = y
        self.display_surface = pygame.display.get_surface()
        self.orientation = orientation

        # Define a fonte e o tamanho da fonte
        self.font = pygame.font.Font(font, self.font_size)

        # Configura a cor do texto (branco)
        self.color = WHITE

        # Cria uma superfície de texto
        self.image = self.font.render(self.text, False, self.color)

        # Obtém o retângulo da superfície de texto
        self.rect = self.image.get_rect()
        if self.orientation == 'topleft':
            self.rect.topleft = (self.x, self.y)
        else:
            self.rect.center = (self.x,self.y)
        
    def draw_box(self,boxSize,boxPos,surface,drawBorder=False,borderWidth=1):
        text_box = pygame.Surface(boxSize)
        text_box_rect = text_box.get_rect(topleft = boxPos)
        self.draw(text_box)
        surface.blit(text_box,text_box_rect)
        if drawBorder:
            pygame.draw.rect(surface,WHITE,text_box_rect,borderWidth)
    
    def new_text(self, new_text):
        self.text = new_text
        self.image = self.font.render(self.text, False, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        
class Button(Text):
    def __init__(self,text,font_size,x,y,font=MAIN_FONT,orientation='topleft'):
        super().__init__(text,font_size,x,y,font=MAIN_FONT)
        
        self.last_clicked_time = 0
        self.is_mouse_pressed = False
        
    def hover(self):
        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos):
            self.image = self.font.render(self.text,False,YELLOW)
        else:
            self.image = self.font.render(self.text,False,WHITE)
            
    def on_click(self):
        self.is_mouse_pressed = True
    
    def release_click(self): self.is_mouse_pressed = False
    
    def update(self):
        self.hover()
        
        

class ScrollingText(Text):
    def __init__(self,text, font_size, x, y,snip,font=MAIN_FONT,):
        super().__init__(text,font_size,x,y,font=MAIN_FONT)
        self.current_text = ""
        self.speed = 0.5
        self.snip = snip
    
    def draw_box(self,boxSize,boxPos,surface,drawBorder=False,borderWidth=1):
        text_box = pygame.Surface(boxSize)
        text_box_rect = text_box.get_rect(topleft = boxPos)
        self.draw_scroll(text_box)
        surface.blit(text_box,text_box_rect)
        if drawBorder:
            pygame.draw.rect(surface,WHITE,text_box_rect,borderWidth)
            
    def draw_scroll(self,surface):
        if self.snip <=len(self.text):
            self.current_text = self.text[:int(self.snip)]
            self.current_image = self.font.render(self.current_text,False,WHITE)
            self.current_rect = self.current_image.get_rect(topleft = (self.x,self.y))
            surface.blit(self.current_image,self.current_rect)
        else:
            surface.blit(self.image,self.rect)
        
        
class TextDisplay:
    def __init__(self, font_size, x, y, max_lines, width, height,font=MAIN_FONT):
        self.font = pygame.font.Font(font, font_size)
        self.x = x
        self.y = y
        self.max_lines = max_lines
        self.width = width
        self.height = height
        self.lines = []
    
    def add_message(self, message):
        self.lines.append(message)
        if len(self.lines) > self.max_lines:
            self.lines.pop(0)
    
    def draw(self, screen):
        text_y = self.y
        for line in self.lines:
            text_surface = self.font.render(line, False, WHITE)
            text_rect = text_surface.get_rect(topleft=(self.x, text_y))
            screen.blit(text_surface, text_rect)
            text_y += text_rect.height

    def clear(self):
        self.lines = []