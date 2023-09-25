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

player_idle = pygame.image.load("img/characters/char_down.png").convert_alpha()
player_rec = player_idle.get_rect(center = (400,300))

player_walk1 = pygame.image.load("img/characters/Walk/Walk1.png").convert_alpha()
player_walk2 = pygame.image.load("img/characters/Walk/Walk2.png").convert_alpha()
player_walk3 = pygame.image.load("img/characters/Walk/Walk3.png").convert_alpha()
player_walk4 = pygame.image.load("img/characters/Walk/Walk4.png").convert_alpha()
player_walk5 = pygame.image.load("img/characters/Walk/Walk5.png").convert_alpha()
player_walk6 = pygame.image.load("img/characters/Walk/walk6.png").convert_alpha()

player_walk = [player_walk1,player_walk2,player_walk3,player_walk4,player_walk5,player_walk6]

player_index = 0

test_font = pygame.font.Font(None,40)

speed = 10

def player_animation():
    global player_idle, player_index
    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
            player_index+=0.1
            if player_index>=len(player_walk): player_index = 0
            player_idle = player_walk[int(player_index)]
           
    


#condição para o loop principal
game_loop = True
        
while game_loop:
    #verifica cada elemento em uma lista de eventos
    for event in pygame.event.get():
        #Verifica se o evento é de saída da janela
        if event.type == pygame.QUIT:
            game_loop = False
    
    pygame.draw.rect(screen,'#4b4860',pygame.Rect(0,0,800,600))
    player_animation()
    screen.blit(player_idle,player_rec)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        player_rec.y-=speed
    
    if keys[pygame.K_DOWN]:
        player_rec.y+=speed
    
    if keys[pygame.K_RIGHT]:
        player_rec.x+=speed
    
    if keys[pygame.K_LEFT]:
        player_rec.x-=speed

    
    #atualiza a tela    
    pygame.display.update() 
    #Taxa de quadros do jogo
    clock.tick(30)
    
 
 
#Sai do Pygame    
pygame.quit()
exit()