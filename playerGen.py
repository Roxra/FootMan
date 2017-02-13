import random
from teamGen import *

class player:
    def __init__(self, name):
        self.name = name
        self.city = 'DefCity'
        self.height = 175
        self.strength = 20.0
        self.defence = 20.0
        self.aggression = 20.0

# Pool of first and last names, grouped by region
british_first = ['David', 'William', 'Robert', 'Daniel', 'John', 'James', 'Micheal', 'Paul', 'Mark']
british_last = ['Smith', 'Johnson', 'Williams', 'Browns', 'Wilson', 'Moore', 'Anderson']

nordic_first = ['Juni', 'Jarel', 'Hjalmar', 'Havelock', 'Hedvig', 'Osvald', 'Ulf', 'Tyw']
nordic_last = ['Jensen', 'Nielsen', 'Hansen', 'Larsen', 'Lund', 'Holm', 'Vestergaard']

german_first = ['Stefan', 'Lukas', 'Niklas', 'Luis', 'Leon', 'Jonas', 'Finn', 'Max', 'Ben', 'Jakob']
german_last = ['Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Becker', 'Klein']

def player_name_gen(club, p):
    if club.city in CITIES_BRITAIN:
        p.name = player_name_randomise(british_first, british_last)
    elif club.city in CITIES_SCANDINAVIA:
        p.name = player_name_randomise(nordic_first, nordic_last)
    elif club.city in CITIES_GERMAN:
        p.name = player_name_randomise(german_first, german_last)

def player_name_randomise(first, last):
    return random.choice(first) + ' ' + random.choice(last)
