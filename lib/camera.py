"""
CameraGroup - Classe de Grupo de Sprites com Funcionalidade de Câmera em Pygame

Módulos:
- pygame: Biblioteca para desenvolvimento de jogos em Python.
- config: Módulo contendo configurações globais.

Classe:
- CameraGroup: Classe derivada de pygame.sprite.Group com funcionalidades de câmera.

Métodos da Classe CameraGroup:
- __init__(): Inicializa a classe CameraGroup. Configura a superfície de exibição e define um deslocamento inicial.
- custom_draw(player): Método personalizado para desenhar sprites na tela considerando um deslocamento (câmera).
    - player: Objeto do tipo Sprite representando o jogador na tela.

Atributos da Classe CameraGroup:
- display_surface: Superfície de exibição obtida a partir do pygame.display.get_surface().
- offset: Vetor 2D (pygame.math.Vector2) representando o deslocamento da câmera em relação ao jogador.

Métodos da Classe CameraGroup (Continuação):
- custom_draw(player): Método personalizado para desenhar sprites na tela considerando um deslocamento (câmera).
    - Itera sobre os sprites no grupo, ordenando-os verticalmente pelo centro de seus retângulos.
    - Calcula a posição relativa do sprite em relação à câmera e o desenha na superfície de exibição.
    - Desenha o sprite do jogador na posição ajustada pela câmera.
"""

import pygame

from lib.config import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)
        
    
    def custom_draw(self,player):
        
        self.offset.x = player.rect.centerx - WIDTH//2
        self.offset.y = player.rect.centery - HEIGHT//2
        for sprite in sorted(self.sprites(),key = lambda sprite:sprite.rect.centery):
            offset_pos = sprite.rect.center - self.offset
            if offset_pos !=0:
                self.display_surface.blit(sprite.image,offset_pos)
                
        player_offset = player.rect.center - self.offset
        self.display_surface.blit(player.image,player_offset)