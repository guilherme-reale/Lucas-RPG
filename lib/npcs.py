import pygame
#Gera NPCs no mapa central
#Um NPC é constituído de uma imagem, de um texto e de uma posição no mapa.
npcs_central = []

npc1 = {'image':"img/NPC_s/NPC-Test.png",
        'pos':(405,195),
        'text':["Lucas, que bom te ver aqui!",
        "Os materiais não reutilizados se tornaram monstros!",
        "Eles estão invadindo nosso mundo.",
        "Apenas esta área está livre deles.",
        "Você precisa lutar contra esses monstros!",
        "Comece indo para leste, na área dos monstros de papelão.",
        "Eles são muito mais fáceis!",
        "E lembre-se: cada monstro, ao ser reciclado, gera tokens.",
        "Esses tokens podem ser utilizados para aplicar magias!",
        "Boa sorte na sua jornada, Lucas!"]}

npcs_central.append(npc1)

npc2 = {'image':"img/NPC_s/NPC Mulher Loira.png", 'pos':(845,580), 'text': ["Aproxime-se da fonte e converse com ela","Você será recompensado!"] }

npcs_central.append(npc2)


        