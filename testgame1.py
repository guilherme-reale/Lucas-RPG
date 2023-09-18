import pygame #importa pygame
from sys import exit #importa comando de saída

#Inicializa pygame
pygame.init()

screen = pygame.display.set_mode((800,400)) #define o tamanho da tela
pygame.display.set_caption('TestGame1') #Define o nome do jogo na janela
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,40)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
font_surface = test_font.render('Testando Pygame',False,'Blue')
        
while True:
    for event in pygame.event.get(): #verifica cada elemento em uma lista de eventos
        if event.type == pygame.QUIT: #Verifica se o evento é de saída da janela
            pygame.quit() #encerra o pygame
            exit() #encerra o python
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(font_surface,(400,200))    
    pygame.display.update() #atualiza a tela
    clock.tick(30)
    
    