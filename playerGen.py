import random
from teamGen import *
from lists import *

class player:
    def __init__(self, name):
        self.name = name
        self.city = 'DefCity'
        self.height = 175
        self.strength = 20.0
        self.defence = 20.0
        self.aggression = 20.0

def player_name_gen(club, p):
    if club.city in CITIES_BRITAIN:
        p.name = two_list_rand(british_first, british_last)
    elif club.city in CITIES_SCANDINAVIA:
        p.name = two_list_rand(nordic_first, nordic_last)
    elif club.city in CITIES_GERMAN:
        p.name = two_list_rand(german_first, german_last)

def two_list_rand(first, last):
    return random.choice(first) + ' ' + random.choice(last)
