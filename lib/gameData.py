import pygame,random

from lib.config import *

player_data = {
    'pos_x':None,
    'pos_y':None,
    'map': MAP_CENTRAL,
    'hp_max':20,
    'hp': 20,
    'atk':10,
    'def':10,
    'coin':20,
    'potion':3,
    'exp':0,
    'lvl':1,
    'time':0 
    
        }

player_data_default = {
    'pos_x':None,
    'pos_y':None,
    'map': MAP_CENTRAL,
    'hp_max':20,
    'hp': 20,
    'atk':10,
    'def':10,
    'coin':0,
    'potion':3,
    'exp':0,
    'lvl':1,
    'time': 0
    
        }

papelao_stats = {
    'hp_max': 20 + random.randint(0,3),
    'atk': 8 + random.randint(0,2),
    'def': 4 + random.randint(0,1),
    'coin': 5,
    'exp': 40
    
    
}

plastico_stats = {
    'hp_max': 30 + random.randint(0,3),
    'atk': 14 + random.randint(0,2),
    'def': 8 + random.randint(0,1),
    'coin': 12,
    'exp': 40
    
    
}

metal_stats = {
    'hp_max': 38 + random.randint(0,5),
    'atk': 22 + random.randint(0,2),
    'def': 14 + random.randint(0,1),
    'coin': 20,
    'exp': 45
    
    
}

toxico_stats = {
    'hp_max': 50 + random.randint(0,3),
    'atk': 22 + random.randint(0,8),
    'def': 12 + random.randint(0,2),
    'coin': 28,
    'exp': 50
    
    
}

boss_stats = {
    'hp_max': 200,
    'atk': 30,
    'def': 20,
    'coin': 20,
    'exp': 65
    
    
}

