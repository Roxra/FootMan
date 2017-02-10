import random
from teamGen import *

def player_name_gen(city):
    british_first = ['David', 'William', 'Robert', 'Daniel', 'John', 'James', 'Micheal', 'Paul', 'Mark']
    british_last = ['Smith', 'Johnson', 'Williams', 'Browns', 'Wilson', 'Moore', 'Anderson']

    nordic_first = []
    nordic_last = []

    german_last = []
    german_last = []

    if city in CITIES_BRITISH:
        name = player_name_randomise(british_first, british_last)
    elif city in CITIES_SCANDINAVIAN:
        name = player_name_randomise(nordic_first, nordic_last)
    elif city in CITIES_GERMAN:
        name = player_name_randomise(german_last, german_last)
    return name

def player_name_randomise(first, last):
    name = random.choice(first) + ' ' + random.choice(last)
    return name
