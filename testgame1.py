#importa pygame
import pygame 
#importa comando de saída
from sys import exit 

#Inicializa pygame
pygame.init()

#define o tamanho da tela
screen = pygame.display.set_mode((800,600)) 

#Define o nome do jogo na janela
pygame.display.set_caption('As Aventuras Ecológicas de Lucas') 

#controla o loop através da taxa de quadros
clock = pygame.time.Clock()

player_img = pygame.image.load("img/characters/char_down.png").convert_alpha()
player_rec = player_img.get_rect(center = (400,300))

test_font = pygame.font.Font(None,40)


#condição para o loop principal
game_loop = True
        
while game_loop:
    #verifica cada elemento em uma lista de eventos
    for event in pygame.event.get():
        #Verifica se o evento é de saída da janela
        if event.type == pygame.QUIT:
            game_loop = False
    
    pygame.draw.rect(screen,'#4b4860',pygame.Rect(0,0,800,600))
    screen.blit(player_img,player_rec)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player_rec.y-=20
    
    if keys[pygame.K_s]:
        player_rec.y+=20
    
    if keys[pygame.K_d]:
        player_rec.x+=20
    
    if keys[pygame.K_a]:
        player_rec.x-=20

    
    #atualiza a tela    
    pygame.display.update() 
    #Taxa de quadros do jogo
    clock.tick(30)
    
 
 
#Sai do Pygame    
pygame.quit()
exit()