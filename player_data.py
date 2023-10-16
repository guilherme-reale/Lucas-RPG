import pygame
import random

player_data = {
    'pos_x':0,
    'pos_y':0,
    'hp_max':20,
    'hp': 20,
    'atk':10,
    'def':10,
    'coins':0,
    'potion':2,
    'exp':0,
    'lvl':1,
    'time':0 
    
        }

plastico_stats = {
    'hp_max': 20 + random.randint(0,3),
    'atk': 10 + random.randint(0,2),
    'def': 5 + random.randint(0,1)
    
    
}