import pygame

import lib.gameData as gameData
from lib.sprites import Npc
from lib.config import *

class MakeNPC:
    def __init__(self):
        self.npc_list = []
    
    def make_list(self):
        if gameData.player_data['map'] == MAP_CENTRAL:
            npc1 = {
                'image': "",
                'pos': (),
                'text': [],
            }
            self.npc_list.append(npc1)
            npc2 = {
                'image': "",
                'pos': (),
                'text': [],
            }
            self.npc_list.append(npc2)
            npc3 = {
                'image': "",
                'pos': (),
                'text': [],
            }
            self.npc_list.append(npc3)
            npc4 = {
                'image': "",
                'pos': (),
                'text': [],
            }
            self.npc_list.append(npc4)
        