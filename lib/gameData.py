import pygame,random

from lib.config import *

player_data = {
    'pos_x':None,
    'pos_y':None,
    'map': MAP_PLASTICO,
    'hp_max':20,
    'hp': 20,
    'atk':10,
    'def':10,
    'coin':0,
    'potion':2,
    'exp':0,
    'lvl':1,
    'time':0 
    
        }

plastico_stats = {
    'hp_max': 20 + random.randint(0,3),
    'atk': 10 + random.randint(0,2),
    'def': 5 + random.randint(0,1),
    'coin': 20,
    'exp': 40
    
    
}