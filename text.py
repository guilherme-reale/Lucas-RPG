import pygame

class Text:
    def __init__(self, text, font_size, x, y):
        self.text = text
        self.font_size = font_size
        self.x = x
        self.y = y
        self.display_surface = pygame.display.get_surface()

        # Define a fonte e o tamanho da fonte
        self.font = pygame.font.Font("font/Pixeltype.ttf", self.font_size)

        # Configura a cor do texto (branco)
        self.color = (255, 255, 255)

        # Cria uma superfície de texto
        self.rendered_text = self.font.render(self.text, True, self.color)

        # Obtém o retângulo da superfície de texto
        self.rect = self.rendered_text.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.rect.topleft)
        