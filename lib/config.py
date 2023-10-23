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

PLAYER_HEIGHT = 17

MAIN_FONT = "font/PixeloidSans-mLxMm.ttf"

PLAYER_IDLE = "img/Personagem Principal/personagem pricipal parado.png"

PLAYER_MOVING = "img/Personagem Principal/personagem pricipal em movimento.png"

PLASTICO = "img/enemies/Plastico.png"

ENEMY_POSITION = (WIDTH/2,100)

POTION_HP = 15

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

RECYCLE_SPRITES = "map/recycle_items.png"

MAP_PLASTICO = 'map/map1.tmx'
MAP_CENTRAL = 'map/map2.tmx'

#mapa do jogo
WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','n','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ','q','r','o','m',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','d','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]
