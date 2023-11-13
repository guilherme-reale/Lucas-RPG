"""
O módulo config contém valores constantes utilizados ao longo de toda a lib.
Separá-los em um arquivo facilita a depuração e modificação do código.
"""



#Largura da janela
WIDTH = 1280
#Altura da janela
HEIGHT = 720
#Taxa de quadros
FPS = 60
#Velocidade do personagem
SPEED = 5
#Tamanho de cada quadrado (tile)
TILESIZE = 64

#Tamanho de cada passo
STEP = 0.1

#Altura do jogador, usada para recortar o usuário no spritesheet
PLAYER_HEIGHT = 17

#Fonte principal do jogo
MAIN_FONT = "font/PixeloidSans-mLxMm.ttf"

#Sprites do personagem principal
PLAYER_IDLE = "img/Personagem Principal/personagem pricipal parado.png"
PLAYER_MOVING = "img/Personagem Principal/personagem pricipal em movimento.png"

#Sprites de decoração
RECYCLE_SPRITES = "img/tilesets/recycle_items.png"


#Arquivos de imagem dos inimigos
PLASTICO = "img/enemies/Plastico.png"
PAPELAO = "img/enemies/Papelao.png"
METAL = "img/enemies/Metal.png"
TOXICO = "img/enemies/Toxico.png"

#Posição do inimigo na tela de batalhas
ENEMY_POSITION = (WIDTH/2,100)

#Qauntidade de HP recuperada pela poção
POTION_HP = 15

#cores
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)




MAP_CENTRAL = 'map/CENTRAL.tmx'
MAP_PLASTICO = 'map/PLASTICO.tmx'
MAP_METAL ="map/METAL.tmx"
MAP_PAPELAO = "map/PAPELAO.tmx"
MAP_TOXICO = "map/TOXICO.tmx"
