import random
from numpy.random import normal
from teamGen import *
from header import *

class player:
    def __init__(self):
        self.name = UNDEF
        self.city = UNDEF
        self.height = STAT_INIT
        self.weight = STAT_INIT
        self.strength = STAT_INIT
        self.effective_strength = STAT_INIT
        self.defence = STAT_INIT
        self.aggression = STAT_INIT
        self.id = ID_NUMBER

def player_create(p):
    # Assign random city, only if there is no currently assigned city
    if p.city == UNDEF:
        p.city = random.choice(CITIES_UNION)
    player_name_gen(p)
    player_stats_gen(p)

def player_name_gen(p):
    if p.city in CITIES_BRITAIN:
        p.name = two_list_rand(british_first, british_last)
    elif p.city in CITIES_SCANDINAVIA:
        p.name = two_list_rand(nordic_first, nordic_last)
    elif p.city in CITIES_GERMAN:
        p.name = two_list_rand(german_first, german_last)

def player_stats_gen(p):
    p.height = round(normal(HEIGHT_DEFAULT, HEIGHT_VARIANCE))
    p.weight = player_weight_gen(p)
    p.strength = normal(STAT_DEFAULT, STAT_VARIANCE)
    p.effective_strength = p.strength + (p.height * p.weight / STR_RATIO)
    p.id = ID_NUMBER
    ID_NUMBER += 1

def two_list_rand(first, last):
    return random.choice(first) + ' ' + random.choice(last)

def player_weight_gen(p):
    # Generates weight using randomised BMI
    bmi = normal(BMI_DEFAULT, BMI_VARIANCE)
    return (bmi * (p.height / 100) ** 2)
