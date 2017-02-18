import random
import numpy as np
from teamGen import *
from lists import *

HEIGHT_DEFAULT = 180
HEIGHT_VARIANCE = 5
BMI_DEFAULT = 75
BMI_VARIANCE = 7
STAT_DEFAULT = 19
STAT_VARIANCE = 6

class player:
    def __init__(self, name):
        self.name = name
        self.city = 'DefCity'
        self.height = HEIGHT_DEFAULT
        self.weight = DEFAULT_WEIGHT
        self.strength = DEFAULT_WEIGHT
        self.defence = STAT_DEFAULT
        self.aggression = STAT_DEFAULT

def player_name_gen(club, p):
    if club.city in CITIES_BRITAIN:
        p.name = two_list_rand(british_first, british_last)
    elif club.city in CITIES_SCANDINAVIA:
        p.name = two_list_rand(nordic_first, nordic_last)
    elif club.city in CITIES_GERMAN:
        p.name = two_list_rand(german_first, german_last)

def player_stats_gen(p):
    p.strength = np.random.normal(STAT_DEFAULT, STAT_VARIANCE)
    p.weight = player_weight_gen(p)
    p.height = round(np.random.normal(HEIGHT_DEFAULT, HEIGHT_VARIANCE))

def two_list_rand(first, last):
    return random.choice(first) + ' ' + random.choice(last)
