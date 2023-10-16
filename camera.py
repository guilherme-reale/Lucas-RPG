import pygame
from config import *

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