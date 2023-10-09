import pygame
from config import *

class Text:
    def __init__(self,text, font_size, x, y,font=MAIN_FONT):
        self.font = font
        self.text = text
        self.font_size = font_size
        self.x = x
        self.y = y
        self.display_surface = pygame.display.get_surface()

        # Define a fonte e o tamanho da fonte
        self.font = pygame.font.Font(font, self.font_size)

        # Configura a cor do texto (branco)
        self.color = WHITE

        # Cria uma superfície de texto
        self.rendered_text = self.font.render(self.text, False, self.color)

        # Obtém o retângulo da superfície de texto
        self.rect = self.rendered_text.get_rect()
        self.rect.topleft = (self.x, self.y)
        
    def draw_box(self,boxSize,boxPos,surface,drawBorder=False,borderWidth=1):
        text_box = pygame.Surface(boxSize)
        text_box_rect = text_box.get_rect(topleft = boxPos)
        self.draw(text_box)
        surface.blit(text_box,text_box_rect)
        if drawBorder:
            pygame.draw.rect(surface,WHITE,text_box_rect,borderWidth)
    
    def new_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, False, self.color)
        self.rect = self.rendered_text.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.rect.topleft)
        
class Buttons(Text):
    def __init__(self,text,font_size,x,y,font=MAIN_FONT):
        super().__init__(text,font_size,x,y,font=MAIN_FONT)
        
        
    def update(self):    
        mousepos = pygame.mouse.get_pos()
        mousekeys = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mousepos):
            self.rendered_text = self.font.render(self.text,False,YELLOW)
            