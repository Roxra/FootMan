import random
import numpy as np
from teamGen import *
from lists import *

HEIGHT_DEFAULT = 180
HEIGHT_VARIANCE = 5
BMI_DEFAULT = 25
BMI_VARIANCE = 2
STAT_DEFAULT = 19
STAT_VARIANCE = 6
STAT_INIT = 0

class player:
    def __init__(self, name):
        self.name = name
        self.city = 'DefCity'
        self.height = STAT_INIT
        self.weight = STAT_INIT
        self.strength = STAT_INIT
        self.defence = STAT_INIT
        self.aggression = STAT_INIT

def player_name_gen(club, p):
    if club.city in CITIES_BRITAIN:
        p.name = two_list_rand(british_first, british_last)
    elif club.city in CITIES_SCANDINAVIA:
        p.name = two_list_rand(nordic_first, nordic_last)
    elif club.city in CITIES_GERMAN:
        p.name = two_list_rand(german_first, german_last)

def player_stats_gen(p):
    p.strength = np.random.normal(STAT_DEFAULT, STAT_VARIANCE)
    p.height = round(np.random.normal(HEIGHT_DEFAULT, HEIGHT_VARIANCE))
    p.weight = player_weight_gen(p)

def two_list_rand(first, last):
    return random.choice(first) + ' ' + random.choice(last)

def player_weight_gen(p):
    # Generate random BMI
    bmi = np.random.normal(BMI_DEFAULT, BMI_VARIANCE)

    # Convert weight to M for calculation, and use BMI converting formula
    weight = bmi * (p.height / 100) ** 2
    return weight
