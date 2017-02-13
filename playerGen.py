import random
import numpy as np
from teamGen import *
from lists import *

DEFAULT_HEIGHT = 180
VARIANCE_HEIGHT = 5
DEFAULT_WEIGHT = 75
VARIANCE_WEIGHT = 7
DEFAULT_STAT = 19
VARIANCE_STAT = 6

class player:
    def __init__(self, name):
        self.name = name
        self.city = 'DefCity'
        self.height = DEFAULT_HEIGHT
        self.weight = DEFAULT_WEIGHT
        self.strength = DEFAULT_WEIGHT
        self.defence = DEFAULT_STAT
        self.aggression = DEFAULT_STAT

def player_name_gen(club, p):
    if club.city in CITIES_BRITAIN:
        p.name = two_list_rand(british_first, british_last)
    elif club.city in CITIES_SCANDINAVIA:
        p.name = two_list_rand(nordic_first, nordic_last)
    elif club.city in CITIES_GERMAN:
        p.name = two_list_rand(german_first, german_last)

def player_stats_gen(p):
    p.strength = np.random.normal(DEFAULT_STAT, VARIANCE_STAT)

    p.height = round(np.random.normal(DEFAULT_HEIGHT, VARIANCE_HEIGHT))

def two_list_rand(first, last):
    return random.choice(first) + ' ' + random.choice(last)
